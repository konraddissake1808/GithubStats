#!/usr/bin/python3

"""
Prints GitHub repository statistics to console for testing
"""

from asyncio import run, set_event_loop_policy, WindowsSelectorEventLoopPolicy
from aiohttp import ClientSession
from os import getenv

from src.github_repo_stats import GitHubRepoStats
from src.env_vars import EnvironmentVariables

# REQUIRED
ACCESS_TOKEN: str = getenv("ACCESS_TOKEN")  # or manually enter ACCESS_TOKEN string
GITHUB_ACTOR: str = getenv("GITHUB_ACTOR")  # or manually enter '<GitHub Username>'

# OPTIONAL
EXCLUDED_REPOS: str = getenv("EXCLUDED")  # or enter: '[owner/repo],...,[owner/repo]'
EXCLUDED_LANGS: str = getenv("EXCLUDED_LANGS")  # or enter: '[lang],...,[lang]'
EXCLUDED_REPO_LANGS: str = getenv(
    "EXCLUDED_REPO_LANGS"
)  # or enter: '[owner/repo],...,[owner/repo]'
IS_INCLUDE_FORKED_REPOS: str = getenv("IS_INCLUDE_FORKED_REPOS")  # or enter: '<bool>'
IS_EXCLUDE_CONTRIB_REPOS: str = getenv("IS_EXCLUDE_CONTRIB_REPOS")  # or enter: '<bool>'
IS_EXCLUDE_ARCHIVE_REPOS: str = getenv("IS_EXCLUDE_ARCHIVE_REPOS")  # or enter: '<bool>'
IS_EXCLUDE_PRIVATE_REPOS: str = getenv("IS_EXCLUDE_PRIVATE_REPOS")  # or enter: '<bool>'
IS_EXCLUDE_PUBLIC_REPOS: str = getenv("IS_EXCLUDE_PUBLIC_REPOS")  # or enter: '<bool>'
REPO_VIEWS: str = getenv("REPO_VIEWS")  # or enter: '<int>'
LAST_VIEWED: str = getenv("LAST_VIEWED")  # or enter: 'YYYY-MM-DD'
FIRST_VIEWED: str = getenv("FIRST_VIEWED")  # or enter: 'YYYY-MM-DD'
IS_MAINTAIN_REPO_VIEWS: str = getenv("IS_STORE_REPO_VIEWS")  # or enter: '<bool>'
MORE_COLLABS: str = getenv("MORE_COLLABS")  # or enter: '<int>'
MORE_REPOS: str = getenv("MORE_REPOS")  # or enter: '[owner/repo],...,[owner/repo]'
ONLY_INCLUDED: str = getenv("ONLY_INCLUDED")  # or enter: '[owner/repo],...'
ONLY_INCLUDED_COLLAB_REPOS: str = getenv(
    "ONLY_INCLUDED_COLLAB_REPOS"
)  # or enter: '[owner/repo],...'
EXCLUDED_COLLAB_REPOS: str = getenv(
    "EXCLUDED_COLLAB_REPOS"
)  # or enter: '[owner/repo],...'
MORE_COLLAB_REPOS: str = getenv("MORE_COLLAB_REPOS")  # or enter: '[owner/repo],...'


async def main() -> None:
    """
    Used for testing
    """
    if not (ACCESS_TOKEN and GITHUB_ACTOR):
        raise RuntimeError(
            "ACCESS_TOKEN and GITHUB_ACTOR environment variables can't be None"
        )

    async with ClientSession() as session:
        stats: GitHubRepoStats = GitHubRepoStats(
            environment_vars=EnvironmentVariables(
                username=GITHUB_ACTOR,
                access_token=ACCESS_TOKEN,
                exclude_repos=EXCLUDED_REPOS,
                exclude_langs=EXCLUDED_LANGS,
                exclude_repo_langs=EXCLUDED_REPO_LANGS,
                is_include_forked_repos=IS_INCLUDE_FORKED_REPOS,
                is_exclude_contrib_repos=IS_EXCLUDE_CONTRIB_REPOS,
                is_exclude_archive_repos=IS_EXCLUDE_ARCHIVE_REPOS,
                is_exclude_private_repos=IS_EXCLUDE_PRIVATE_REPOS,
                is_exclude_public_repos=IS_EXCLUDE_PUBLIC_REPOS,
                repo_views=REPO_VIEWS,
                repo_last_viewed=LAST_VIEWED,
                repo_first_viewed=FIRST_VIEWED,
                is_store_repo_view_count=IS_MAINTAIN_REPO_VIEWS,
                more_collaborators=MORE_COLLABS,
                manually_added_repos=MORE_REPOS,
                only_included_repos=ONLY_INCLUDED,
                only_included_collab_repos=ONLY_INCLUDED_COLLAB_REPOS,
                exclude_collab_repos=EXCLUDED_COLLAB_REPOS,
                more_collab_repos=MORE_COLLAB_REPOS,
            ),
            session=session,
        )
        print(await stats.to_str())


if __name__ == "__main__":
    set_event_loop_policy(policy=WindowsSelectorEventLoopPolicy())
    run(main=main())
