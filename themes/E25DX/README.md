---title: "Overview"
  url: "docs/overview"
  aliases:
  - "/docs"
---

  Overview
  ```

- Add `newsite/content/en/docs/a1.hello-world.md` as the first page of first section

  ```markdown
  ---
  title: Hello World
  slug: hello-world
  ---

  Hello World
  ```

- Add `newsite/content/en/docs/b1.modules.md` as the first page of the second section

  ```markdown
  ---
  title: Modules
  slug: modules
  ---

  Module
  ```

- Add `newsite/data/en/docs/sidebar.yml` for section titles and page titles

  ```markdown
  - title: Documentation
    pages:
      - title: Overview

  - title: Basics
    pages:
      - title: Hello World

  - title: Beyond The Basics
    pages:
      - title: Modules
  ```

#### 4. Sample blog

- Add `newsite/content/en/blog/2026_1_hello_world/index.md`

  ```markdown
  ---
  title: Hello World
  slug: "hello-world"
  summary: Hello World Summary
  ---

  Hello World
  ```

- Add any image of png (or jpg) for `newsite/content/en/blog/2026_1_hello_world/cover.png` for blog post cover image

#### 5. Sample page

- Add `newsite/content/en/page/about/index.md` for about page

  ```markdown
  ---
  title: About
  url: "about"
  ---

  About
  ```

- Add any image of png (or jpg) for `newsite/content/en/page/about/cover.png` for about page cover image

#### 6. Main menu

- Update `newsite/hugo.yaml` to add menu configurations

  ```markdown
  menus:
    main:
      - identifier: home
        name: Home
        pre: <i aria-hidden>🏡</i>
        pageRef: /
        weight: 1
      - identifier: docs
        name: Docs
        pre: <i aria-hidden>📖</i>
        pageRef: /docs
        weight: 2
      - identifier: blog
        name: Blog
        pre: <i aria-hidden>🖊️</i>
        pageRef: /blog
        weight: 3
      - identifier: about
        name: About
        pre: <i aria-hidden>🧑‍💻</i>
        pageRef: /page/about
        weight: 4
  ```

#### 7. Run and build the site for production.

- Run `hugo server` to preview the site.

  > 💡 If you see `ERROR Failed to read Git log: fatal: your current branch 'main' does not have any commits yet`,
  > Change `newsite/hugo.yaml` -> `enableGitInfo: false` (if you want to run `hugo server` before commit the changes.)

- Run `hugo build --minify ` to build the site for production.

---

[![buymeacoffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-dumindu-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=ffffff&labelColor=333333)](https://www.buymeacoffee.com/dumindu)