# 📈 [GitHub Stats Visualization](https://github.com/R055A/GitStats) 🔭

Generate regularly updated visualizations of user and repository statistics from the GitHub [GraphQL](https://docs.github.com/en/graphql) and [REST](https://docs.github.com/en/rest) APIs using GitHub [Actions](https://docs.github.com/en/actions) and [Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets). Customizable visualizations support dark and light mode and can adapt to device sizes.

> A modification of [`jstrieb/github-stats`](https://github.com/jstrieb/github-stats) visualizations with new and improved statistics and more options!

[![GitStats Overview](https://raw.githubusercontent.com/R055A/GitStats/actions_branch/generated_images/overview.svg)![GitStats Languages](https://raw.githubusercontent.com/R055A/GitStats/actions_branch/generated_images/languages.svg)](https://github.com/R055A/GitStats)

> _Note: my '**Avg contributions**' stats is customized to only consider collaborative [university project repos](https://github.com/University-Project-Repos)_

## Description of Statistical Terminology

| GitHub Statistics Term         | Description                                                                                                    |
|--------------------------------|----------------------------------------------------------------------------------------------------------------|
| All-time GitHub contributions  | Count of all contributions ([as defined by GitHub](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/managing-contribution-settings-on-your-profile/viewing-contributions-on-your-profile)) to any and all repositories any time for a given user |
| Lines of code changes*         | Sum of all code additions and deletions to all repositories contributed to for a user, measured by lines       |
| Avg contributions [weighted]*  | Average code changes per collaborative repository for a user [weighted relative to contributor count]          |
| Repos contributed [% collab]*  | Count of all repositories contributed to by a user [including percent in collaboration with others]            |
| Repo views (as of YYYY-MM-DD)* | Sum of views to all repositories since created, if owned, or contributed to (from a given date)                | 
| Repo collaborators*            | Sum of collaborator and contributor counts for all repositories contributed to or owned for a user             |
| Repo forks*                    | Sum of all-time fork counts for all repositories contributed to or owned for a user                            |
| Repo stars*                    | Sum of all-time star counts for all repositories contributed to or owned for a user                            |
| # [+#] Implemented Languages*  | Listed [and hidden] percentages of implemented languages relative to sizes of files contributed to             |

> \* Customisable as instructed in the :closed_lock_with_key: Options section below

# :rocket: Instructions

<details>
<summary>Click drop-down to view step-by-step instructions for generating your own GitHub statistics visualizations
</summary>

### Copy Repository

1. Click either link to start generating your own GitHub statistic visualizations: 
   1. [Generate your own copy of this repository without the commit history](https://github.com/R055A/GitStats/generate)
      * *Note: the first GitHub Actions workflow initiated at creation of the copied repository is expected to fail*
   2. [Fork a copy of this repository with the commit history configured to sync changes](https://github.com/R055A/GitStats/fork)
      * *Note: this copies all branches including the `action_branch` with statistics, but this can be overwritten*

### Generate a New Personal Access Token

2. Generate a personal access token by following these steps:
   1. If you are logged in, click this link to: [generate a new "classic" token](https://github.com/settings/tokens/new)
      * *Otherwise, to learn how to generate a personal access token: [read these instructions](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)*
   2. Ensure it is a "classic" token being generated and not a "fine-grained" token
   2. Name the token
   3. Select your preferred '***Expiration***' date
   4. Select `repo` for '<u>**Full control of private repositories**</u>'
   5. Select `read:user` to '<u>**Read only ALL user profile data**</u>'
   6. Click the '***Generate token***' button
   7. Copy the generated token - there is only one opportunity provided for this

### Create ACCESS_TOKEN Secret

3. Create a repository secret for the personal access token by following these steps:
   1. If this is your copy of the repository, click this link to: [create a new secret](../../settings/secrets/actions/new)
      * *Otherwise, go to repository **Settings**, click the **Secrets** option, then click **New repository secret***
   2. Name the new secret: `ACCESS_TOKEN`
   3. Enter the generated **[personal access token](#generate-a-new-personal-access-token)** as the '*Value*'

### Run GitHub Actions Workflow

4. Manually generate GitHub statistics visualizations:
   1. This can be done using any of the following two GitHub Actions workflows:
      1. For the **first time**, or to **reset stored statistics** (although this is done with every push to the main):
         * Click the link to: [go to the **Generate Git Stats Images** GitHub Actions workflow](../../actions/workflows/non_auto_generate_stat_images.yml)
         > *This is required if the `actions_branch` branch is not created, as it is created when run*
      2. Otherwise, for **updating** generated statistics visualizations (although this is automatically done ):
         * Click the link to: [go to the **Auto Update Stats Images** GitHub Actions workflow](../../actions/workflows/auto_update_stat_images.yml)
         > *This requires the `actions_branch` branch to first be created with generated statistics visualizations*
   2. With the GitHub Actions page open, click the '***Run workflow***' dropdown menu button
   3. Select `Branch: main` from the '***Use workflow from***' dropdown list
   4. Click the '***Run workflow***' button
       * _Note: this could take some time_

### View Generated Statistics

5. Following the successful completion of a workflow, generated statistics visualizations can be viewed:
   1. In the `generated_images` directory in the `actions_branch` branch with the following image links:
      1. [Language statistics](../../blob/actions_branch/generated_images/languages.svg)
      2. [Overview statistics](../../blob/actions_branch/generated_images/overview.svg)

### Display Generated Statistics

6. To display the generated statistics, static URLs can be used for images that are updated weekly:
   1. For generated language statistics visualizations (replacing `<username>` with your GitHub username):
   ```md
   ![](https://raw.githubusercontent.com/<username>/GitStats/actions_branch/generated_images/languages.svg)
   ```
   2. For generated overview statistic visualizations (replacing `<username>` with your GitHub username):
   ```md
   ![](https://raw.githubusercontent.com/<username>/GitStats/actions_branch/generated_images/overview.svg)
   ```
   
</details>

# :closed_lock_with_key: Options

<details>
<summary>Click drop-down to view optional repository Secrets for customizing GitHub statistic visualizations
</summary>

* ### Optional Secret *Name*: `EXCLUDED`
  For excluding repositories from being included entirely in the generated statistic visualizations.
  
  **Instructions**:
  * enter *Value* in the following format (separated by commas):
    * `[owner/repo],[owner/repo],...,[owner/repo]`
  * example:
    * `jstrieb/github-stats,rahul-jha98/github-stats-transparent,idiotWu/stats`
* ### Optional Secret *Name*: `ONLY_INCLUDED`
  For **ONLY** including repositories in the generated statistic visualizations
    - such as when there are fewer repositories to include than to exclude
  
    **Instructions**:
    * enter *Value* in the following format (separated by commas):
      * `[owner/repo],[owner/repo],...,[owner/repo]`
    * example:
      * `R055A/GitStats,R055A/R055A`
* ### Optional Secret *Name*: `EXCLUDED_LANGS`
  For excluding undesired languages from being included in the generated statistic visualizations
  
  **Instructions**:
  * enter *Value* in the following format (separated by commas):
    * `[language],[language],...,[language]`
  * example:
    * `HTML,Jupyter Notebook,Makefile,Dockerfile`
* ### Optional Secret *Name*: `EXCLUDED_REPO_LANGS`
  For excluding any/all language statistics specific to a repository from being included in the generated visualizations
  
  **Instructions**:
  * enter *Value* in the following format (separated by commas):
    * `[owner/repo--language...--language],[owner/repo--language...--language],...,[owner/repo--language...--language]`
    * `--language` denotes a language in the repository to be excluded from stats or exclude this for all repo languages
  * example:
    * `jstrieb/github-stats--python,rahul-jha98/github-stats-transparent,idiotWu/stats--python--shell`
* ### Optional Secret *Name*: `IS_INCLUDE_FORKED_REPOS`
  Boolean option for including forked repositories in the generated statistic visualizations. These could repeat statistical calculations
    - `false` by default

  **Instructions**:
  * enter *Value* in the following format:
    * `<boolean>`
  * examples:
    * `true`
* ### Optional Secret *Name*: `IS_EXCLUDE_CONTRIB_REPOS`
  Boolean option for excluding non-owned repositories contributed to in the generated statistic visualizations
    - `false` by default

  **Instructions**:
  * enter *Value* in the following format:
    * `<boolean>`
  * examples:
    * `true`
* ### Optional Secret *Name*: `IS_EXCLUDE_ARCHIVE_REPOS`
  Boolean option for excluding archived repositories in the generated statistic visualizations
    - `false` by default
    
  **Instructions**:
  * enter *Value* in the following format:
    * `<boolean>`
  * examples:
    * `true`
* ### Optional Secret *Name*: `IS_EXCLUDE_PRIVATE_REPOS`
  Boolean option for excluding private repositories in the generated statistic visualizations
    - for when you want to keep those secrets locked away from prying eyes
    - `false` by default
    
  **Instructions**:
  * enter *Value* in the following format:
    * `<boolean>`
  * examples:
    * `true`
* ### Optional Secret *Name*: `IS_EXCLUDE_PUBLIC_REPOS`
  Boolean option for excluding public repositories in the generated statistic visualizations
    - `false` by default
    
  **Instructions**:
  * enter *Value* in the following format:
    * `<boolean>`
  * examples:
    * `true`
* ### Optional Secret *Name*: `MORE_REPOS`
  For including repositories that are otherwise not included in generated statistic visualizations when scraping by username
    - such as repositories imported from, say, GitLab - hint: add emails used in imported repo commits to profile settings
    
  **Instructions**:
  * enter *Value* in the following format (separated by commas):
    * `[owner/repo],[owner/repo],...,[owner/repo]`
  * example:
    * `R055A/GitStats,R055A/R055A`
* ### Optional Secret *Name*: `MORE_COLLABS`
  For adding a constant value to the generated repository collaborators statistic
    - such as for collaborators that are otherwise not represented
    
  **Instructions**:
  * enter *Value* in the following format:
    * `<int>`
  * example:
    * `4`
* ### Optional Secret *Name*: `ONLY_INCLUDED_COLLAB_REPOS`
  For **ONLY** including collaborative repositories in the generated average contribution statistics calculations
    - such as when there are fewer collaborative repositories to include than to exclude
  
    **Instructions**:
    * enter *Value* in the following format (separated by commas):
      * `[owner/repo],[owner/repo],...,[owner/repo]`
    * example:
      * `R055A/UniversityProject-A,R055A/UniversityProject-B`
* ### Optional Secret *Name*: `EXCLUDED_COLLAB_REPOS`
  For excluding collaborative repositories from being included in the average contribution statistics calculations
    - for example, such as for when 
      - contributions are made to a collaborative repo, but it is not one of your projects (open-source typo fix, etc)
      - someone deletes and re-adds the entire codebase a few times too many
      - your or someone else's performance is not fairly represented - missing data bias 
      - pirates, ninjas, etc.

  **Instructions**:
  * enter *Value* in the following format (separated by commas):
    * `[owner/repo],[owner/repo],...,[owner/repo]`
  * example:
    * `tera_open_source/bit_typo_fix,peer_repo/missing_or_no_git_co_author_credit,dude_collab/email_not_reg_on_github,dog_ate/my_repo,mars/attacks`
* ### Optional Secret *Name*: `MORE_COLLAB_REPOS`
    For including collaborative repositories that are otherwise not included in the average contribution statistics calculations
    - for example, such as when
      - nobody even bothered to join the repository as a collaborator let alone contribute anything
      - the repository is imported and because it is ghosted there are no other contributions and, thus, none of the other collaborators are represented in the scraping

  **Instructions**:
  * enter *Value* in the following format (separated by commas):
    * `[owner/repo],[owner/repo],...,[owner/repo]`
  * example:
    * `imported_ghosted/large_A+_collab_project,slave_trade/larger_A++_project`
* ### Optional Secret *Name*: `IS_STORE_REPO_VIEWS`
  Boolean for storing generated repository view statistic visualization data beyond the 14 day-limit GitHub API allows 
    - `true` by default

  **Instructions**:
  * enter *Value* in the following format:
    * `<boolean>`
  * examples:
    * `false`
* ### Optional Secret *Name*: `REPO_VIEWS`
  For adding a constant value to the generated repository view statistics
    - such as for when the stored data is reset or when importing stat data from elsewhere
    - requires being removed within 14 days after the first workflow is run (with `LAST_VIEWED`)
    - requires corresponding `LAST_VIEWED` and `FIRST_VIEWED` Secrets
    
  **Instructions**:
  * enter *Value* in the following format:
    * `<int>`
  * example:
    * `5000`
* ### Optional Secret *Name*: `LAST_VIEWED`
  For updating the date the generated repository view statistics data is added to storage from
    - such as for when the stored data is reset or when importing stat data from elsewhere
    - requires being removed within 14 days after the first workflow is run (with `REPO_VIEWS`)
    - may require corresponding `REPO_VIEWS` and `FIRST_VIEWED` Secrets
    
  **Instructions**:
  * enter *Value* in the following format:
    * `YYYY-MM-DD`
  * example:
    * `2020-10-01`
* ### Optional Secret *Name*: `FIRST_VIEWED`
  For updating the '*as of*' date the generated repository view statistics data is stored from
    - such as for when the stored data is reset or when importing stat data from elsewhere
    - may require corresponding `REPO_VIEWS` and `LAST_VIEWED` Secrets
    
  **Instructions**:
  * enter *Value* in the following format:
    * `YYYY-MM-DD`
  * example:
    * `2021-03-31`
</details>

# :green_heart: Support the Project

There are a few things you can do to support the project:

- ✨ Star this repository (and/or 🌠 star [`jstrieb/github-stats`](https://github.com/jstrieb/github-stats) and 🔭 follow [`jstrieb`](https://github.com/jstrieb) for more)
- :memo: Report any bugs :bug:, glitches, or errors that you find :monocle_face:
- :money_with_wings: Spare a donation to a worthy cause 🥹
