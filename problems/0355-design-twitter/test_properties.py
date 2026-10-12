from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Twitter = load_module("0355-design-twitter").Twitter


@given(
    st.lists(
        st.tuples(st.integers(0, 3), st.integers(1, 5), st.integers(1, 5)), min_size=1, max_size=120
    )
)
def test_social_sequence_matches_global_post_log(actions):
    app = Twitter()
    posts = []
    follows = set()
    tweet = 0
    for operation, user, other in actions:
        if operation == 0:
            tweet += 1
            posts.append((user, tweet))
            assert app.postTweet(user, tweet) is None
        elif operation == 1 and user != other:
            follows.add((user, other))
            assert app.follow(user, other) is None
        elif operation == 2 and user != other:
            follows.discard((user, other))
            assert app.unfollow(user, other) is None
        else:
            expected = [
                id for author, id in reversed(posts) if author == user or (user, author) in follows
            ][:10]
            assert app.getNewsFeed(user) == expected
