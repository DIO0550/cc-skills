# READMEバッジ完全ガイド

プロジェクトのステータス、品質、統計を視覚的に表示するバッジの包括的なガイド。

## 目次

1. [バッジの基本](#バッジの基本)
2. [ビルドとCI/CD](#ビルドとcicd)
3. [カバレッジとテスト](#カバレッジとテスト)
4. [バージョンとリリース](#バージョンとリリース)
5. [ダウンロードと使用状況](#ダウンロードと使用状況)
6. [ライセンス](#ライセンス)
7. [依存関係](#依存関係)
8. [コード品質](#コード品質)
9. [ソーシャルとコミュニティ](#ソーシャルとコミュニティ)
10. [カスタムバッジ](#カスタムバッジ)

---

## バッジの基本

### バッジとは？

バッジは、プロジェクトのステータス、品質、統計情報を視覚的に表示する小さな画像です。

### なぜバッジを使用するか？

- ✅ プロジェクトの健全性を即座に表示
- 📊 重要な指標を一目で提供
- 🎨 READMEを視覚的に魅力的に
- 🏆 品質と信頼性を示す

### バッジの配置

```markdown
# プロジェクト名

[![バッジ1](URL)](リンク)
[![バッジ2](URL)](リンク)
[![バッジ3](URL)](リンク)

> プロジェクトの説明
```

### Shields.ioの使用

ほとんどのバッジは [shields.io](https://shields.io) を使用します：

**基本構文:**
```
https://img.shields.io/badge/ラベル-メッセージ-色
```

**例:**
```markdown
![カスタムバッジ](https://img.shields.io/badge/ステータス-安定-green)
```

---

## ビルドとCI/CD

### GitHub Actions

```markdown
[![ビルドステータス](https://github.com/username/repo/workflows/CI/badge.svg)](https://github.com/username/repo/actions)
```

**特定のブランチ:**
```markdown
[![ビルド](https://github.com/username/repo/workflows/CI/badge.svg?branch=main)](https://github.com/username/repo/actions)
```

### Travis CI

```markdown
[![Travis CI](https://travis-ci.org/username/repo.svg?branch=main)](https://travis-ci.org/username/repo)
```

### CircleCI

```markdown
[![CircleCI](https://circleci.com/gh/username/repo.svg?style=svg)](https://circleci.com/gh/username/repo)
```

### Jenkins

```markdown
[![Jenkins](https://img.shields.io/jenkins/build?jobUrl=https://jenkins.example.com/job/project)](https://jenkins.example.com)
```

### GitLab CI

```markdown
[![GitLab CI](https://gitlab.com/username/repo/badges/main/pipeline.svg)](https://gitlab.com/username/repo/-/commits/main)
```

### Azure Pipelines

```markdown
[![Azure](https://dev.azure.com/username/project/_apis/build/status/repo)](https://dev.azure.com/username/project/_build)
```

---

## カバレッジとテスト

### Codecov

```markdown
[![Codecov](https://codecov.io/gh/username/repo/branch/main/graph/badge.svg)](https://codecov.io/gh/username/repo)
```

### Coveralls

```markdown
[![Coveralls](https://coveralls.io/repos/github/username/repo/badge.svg?branch=main)](https://coveralls.io/github/username/repo?branch=main)
```

### Code Climate

```markdown
[![Code Climate](https://api.codeclimate.com/v1/badges/abc123/test_coverage)](https://codeclimate.com/github/username/repo/test_coverage)
```

### 手動カバレッジバッジ

```markdown
[![カバレッジ](https://img.shields.io/badge/カバレッジ-90%25-brightgreen)](https://github.com/username/repo)
```

---

## バージョンとリリース

### npm

```markdown
[![npm version](https://img.shields.io/npm/v/package-name.svg)](https://www.npmjs.com/package/package-name)
```

### PyPI

```markdown
[![PyPI](https://img.shields.io/pypi/v/package-name.svg)](https://pypi.org/project/package-name/)
```

**Python バージョン:**
```markdown
[![Python](https://img.shields.io/pypi/pyversions/package-name.svg)](https://pypi.org/project/package-name/)
```

### RubyGems

```markdown
[![Gem Version](https://img.shields.io/gem/v/gem-name.svg)](https://rubygems.org/gems/gem-name)
```

### Crates.io (Rust)

```markdown
[![Crates.io](https://img.shields.io/crates/v/crate-name.svg)](https://crates.io/crates/crate-name)
```

### Maven Central

```markdown
[![Maven Central](https://img.shields.io/maven-central/v/com.example/artifact-id.svg)](https://search.maven.org/artifact/com.example/artifact-id)
```

### NuGet (.NET)

```markdown
[![NuGet](https://img.shields.io/nuget/v/package-name.svg)](https://www.nuget.org/packages/package-name/)
```

### Packagist (PHP)

```markdown
[![Packagist](https://img.shields.io/packagist/v/vendor/package.svg)](https://packagist.org/packages/vendor/package)
```

### GitHub Release

```markdown
[![GitHub release](https://img.shields.io/github/release/username/repo.svg)](https://github.com/username/repo/releases)
```

**リリース日付:**
```markdown
[![GitHub Release Date](https://img.shields.io/github/release-date/username/repo.svg)](https://github.com/username/repo/releases)
```

---

## ダウンロードと使用状況

### npm ダウンロード

```markdown
[![npm downloads](https://img.shields.io/npm/dt/package-name.svg)](https://www.npmjs.com/package/package-name)
```

**月間ダウンロード:**
```markdown
[![npm](https://img.shields.io/npm/dm/package-name.svg)](https://www.npmjs.com/package/package-name)
```

### PyPI ダウンロード

```markdown
[![PyPI downloads](https://img.shields.io/pypi/dm/package-name.svg)](https://pypi.org/project/package-name/)
```

### Docker Pulls

```markdown
[![Docker Pulls](https://img.shields.io/docker/pulls/username/image-name.svg)](https://hub.docker.com/r/username/image-name)
```

### GitHub ダウンロード

```markdown
[![GitHub downloads](https://img.shields.io/github/downloads/username/repo/total.svg)](https://github.com/username/repo/releases)
```

### Chrome Web Store

```markdown
[![Chrome Web Store](https://img.shields.io/chrome-web-store/users/extension-id.svg)](https://chrome.google.com/webstore/detail/extension-id)
```

---

## ライセンス

### 標準ライセンスバッジ

```markdown
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
```

### 各種ライセンス

**MIT:**
```markdown
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
```

**Apache 2.0:**
```markdown
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
```

**GPL v3:**
```markdown
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
```

**BSD:**
```markdown
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
```

**ISC:**
```markdown
[![License: ISC](https://img.shields.io/badge/License-ISC-blue.svg)](https://opensource.org/licenses/ISC)
```

### GitHub ライセンス検出

```markdown
[![License](https://img.shields.io/github/license/username/repo.svg)](LICENSE)
```

---

## 依存関係

### 依存関係のステータス

**npm:**
```markdown
[![Dependencies](https://img.shields.io/david/username/repo.svg)](https://david-dm.org/username/repo)
```

**Dev Dependencies:**
```markdown
[![Dev Dependencies](https://img.shields.io/david/dev/username/repo.svg)](https://david-dm.org/username/repo?type=dev)
```

### セキュリティ脆弱性

**Snyk:**
```markdown
[![Known Vulnerabilities](https://snyk.io/test/github/username/repo/badge.svg)](https://snyk.io/test/github/username/repo)
```

**npm audit:**
```markdown
[![npm audit](https://img.shields.io/npm/audit/package-name.svg)](https://www.npmjs.com/package/package-name)
```

### 依存関係の更新

**Dependabot:**
```markdown
[![Dependabot Status](https://api.dependabot.com/badges/status?host=github&repo=username/repo)](https://dependabot.com)
```

---

## コード品質

### Code Climate

**メンテナビリティ:**
```markdown
[![Maintainability](https://api.codeclimate.com/v1/badges/abc123/maintainability)](https://codeclimate.com/github/username/repo/maintainability)
```

### Codacy

```markdown
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/abc123)](https://www.codacy.com/app/username/repo)
```

### CodeFactor

```markdown
[![CodeFactor](https://www.codefactor.io/repository/github/username/repo/badge)](https://www.codefactor.io/repository/github/username/repo)
```

### SonarCloud

```markdown
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=username_repo&metric=alert_status)](https://sonarcloud.io/dashboard?id=username_repo)
```

### Scrutinizer

```markdown
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/username/repo/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/username/repo/?branch=main)
```

---

## ソーシャルとコミュニティ

### GitHub Stars

```markdown
[![GitHub stars](https://img.shields.io/github/stars/username/repo.svg?style=social)](https://github.com/username/repo/stargazers)
```

### GitHub Forks

```markdown
[![GitHub forks](https://img.shields.io/github/forks/username/repo.svg?style=social)](https://github.com/username/repo/network)
```

### GitHub Watchers

```markdown
[![GitHub watchers](https://img.shields.io/github/watchers/username/repo.svg?style=social)](https://github.com/username/repo/watchers)
```

### Twitter

```markdown
[![Twitter Follow](https://img.shields.io/twitter/follow/username.svg?style=social)](https://twitter.com/username)
```

### Discord

```markdown
[![Discord](https://img.shields.io/discord/123456789.svg?label=Discord&logo=discord)](https://discord.gg/invite)
```

### Gitter

```markdown
[![Gitter](https://badges.gitter.im/username/repo.svg)](https://gitter.im/username/repo)
```

### Slack

```markdown
[![Slack](https://img.shields.io/badge/slack-join-brightgreen.svg)](https://slack-invite-url.com)
```

---

## プロジェクト情報

### リポジトリサイズ

```markdown
[![Repo Size](https://img.shields.io/github/repo-size/username/repo.svg)](https://github.com/username/repo)
```

### コード行数

```markdown
[![Lines of Code](https://img.shields.io/tokei/lines/github/username/repo)](https://github.com/username/repo)
```

### 最終コミット

```markdown
[![Last Commit](https://img.shields.io/github/last-commit/username/repo.svg)](https://github.com/username/repo/commits/main)
```

### コントリビューター数

```markdown
[![Contributors](https://img.shields.io/github/contributors/username/repo.svg)](https://github.com/username/repo/graphs/contributors)
```

### Issues

**オープンissues:**
```markdown
[![GitHub issues](https://img.shields.io/github/issues/username/repo.svg)](https://github.com/username/repo/issues)
```

**クローズされたissues:**
```markdown
[![GitHub issues closed](https://img.shields.io/github/issues-closed/username/repo.svg)](https://github.com/username/repo/issues?q=is%3Aissue+is%3Aclosed)
```

### プルリクエスト

```markdown
[![GitHub pull requests](https://img.shields.io/github/issues-pr/username/repo.svg)](https://github.com/username/repo/pulls)
```

### コミットアクティビティ

```markdown
[![Commit Activity](https://img.shields.io/github/commit-activity/m/username/repo.svg)](https://github.com/username/repo/commits/main)
```

---

## プラットフォーム固有

### Node.js バージョン

```markdown
[![Node.js Version](https://img.shields.io/node/v/package-name.svg)](https://nodejs.org)
```

### プラットフォームサポート

```markdown
[![Platform](https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-lightgrey)](https://github.com/username/repo)
```

### ブラウザサポート

```markdown
[![Browser Support](https://img.shields.io/badge/browser-chrome%20%7C%20firefox%20%7C%20safari-brightgreen)](https://github.com/username/repo)
```

---

## ドキュメント

### Read the Docs

```markdown
[![Documentation Status](https://readthedocs.org/projects/project-name/badge/?version=latest)](https://project-name.readthedocs.io/)
```

### GitHub Pages

```markdown
[![GitHub Pages](https://img.shields.io/badge/docs-github--pages-blue)](https://username.github.io/repo)
```

### Swagger/OpenAPI

```markdown
[![Swagger Validator](https://img.shields.io/swagger/valid/3.0?specUrl=https%3A%2F%2Fapi.example.com%2Fswagger.json)](https://api.example.com/docs)
```

---

## カスタムバッジ

### 静的バッジ

**基本:**
```markdown
![Custom](https://img.shields.io/badge/ラベル-メッセージ-色)
```

**例:**
```markdown
![Status](https://img.shields.io/badge/ステータス-安定版-green)
![Version](https://img.shields.io/badge/バージョン-2.0.0-blue)
![PRs](https://img.shields.io/badge/PRs-歓迎-brightgreen)
```

### 色の選択

利用可能な色：
- `brightgreen`
- `green`
- `yellowgreen`
- `yellow`
- `orange`
- `red`
- `blue`
- `lightgrey`
- `blueviolet`

**Hex色:**
```markdown
![Custom](https://img.shields.io/badge/ラベル-メッセージ-ff69b4)
```

### ロゴの追加

```markdown
![NPM](https://img.shields.io/badge/npm-v8.0.0-CB3837?logo=npm)
![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python)
![Docker](https://img.shields.io/badge/Docker-20.10-2496ED?logo=docker)
```

**利用可能なロゴ:** [Simple Icons](https://simpleicons.org/)を確認

### スタイル

```markdown
<!-- フラット（デフォルト） -->
![Flat](https://img.shields.io/badge/スタイル-フラット-blue)

<!-- フラットスクエア -->
![Flat Square](https://img.shields.io/badge/スタイル-フラットスクエア-blue?style=flat-square)

<!-- Plastic -->
![Plastic](https://img.shields.io/badge/スタイル-plastic-blue?style=plastic)

<!-- For the Badge -->
![For the Badge](https://img.shields.io/badge/スタイル-for%20the%20badge-blue?style=for-the-badge)

<!-- Social -->
![Social](https://img.shields.io/github/stars/username/repo?style=social)
```

---

## バッジのベストプラクティス

### 選択のガイドライン

1. **関連性のあるバッジのみ**
   - ✅ ビルドステータス、カバレッジ、バージョン
   - ❌ 無関係または時代遅れのバッジ

2. **適切な数を保つ**
   - ✅ 3-8個のバッジ
   - ❌ 15個以上のバッジ

3. **重要なものを優先**
   - まずビルドステータス
   - 次にバージョン
   - 最後にソーシャル

4. **正確性を維持**
   - リンク切れを避ける
   - バッジを最新に保つ
   - 非推奨のサービスを削除

### 配置のヒント

**水平配置:**
```markdown
[![Badge1](url1)](link1) [![Badge2](url2)](link2) [![Badge3](url3)](link3)
```

**垂直配置:**
```markdown
[![Badge1](url1)](link1)
[![Badge2](url2)](link2)
[![Badge3](url3)](link3)
```

**グループ化:**
```markdown
<!-- ビルドと品質 -->
[![Build](...)](#) [![Coverage](...)](#) [![Quality](...)](#)

<!-- バージョンとダウンロード -->
[![Version](...)](#) [![Downloads](...)](#)

<!-- ソーシャル -->
[![Stars](...)](#) [![Forks](...)](#)
```

### アクセシビリティ

**代替テキストを追加:**
```markdown
[![ビルドステータス - 成功](https://...)](...)
```

**スクリーンリーダー向け:**
```markdown
<a href="...">
  <img src="..." alt="ビルドステータス: 合格">
</a>
```

---

## 完全な例

### 最小限のREADME

```markdown
# プロジェクト名

[![ビルド](https://github.com/user/repo/workflows/CI/badge.svg)](https://github.com/user/repo/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> プロジェクトの説明
```

### 標準的なREADME

```markdown
# プロジェクト名

[![ビルド](https://github.com/user/repo/workflows/CI/badge.svg)](https://github.com/user/repo/actions)
[![カバレッジ](https://codecov.io/gh/user/repo/badge.svg)](https://codecov.io/gh/user/repo)
[![バージョン](https://img.shields.io/npm/v/package.svg)](https://www.npmjs.com/package/package)
[![ダウンロード](https://img.shields.io/npm/dm/package.svg)](https://www.npmjs.com/package/package)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> プロジェクトの説明
```

### 包括的なREADME

```markdown
# プロジェクト名

<!-- ビルドと品質 -->
[![ビルド](https://github.com/user/repo/workflows/CI/badge.svg)](https://github.com/user/repo/actions)
[![カバレッジ](https://codecov.io/gh/user/repo/badge.svg)](https://codecov.io/gh/user/repo)
[![Code Quality](https://api.codeclimate.com/v1/badges/.../maintainability)](https://codeclimate.com/github/user/repo)

<!-- パッケージ -->
[![npm](https://img.shields.io/npm/v/package.svg)](https://www.npmjs.com/package/package)
[![npm downloads](https://img.shields.io/npm/dm/package.svg)](https://www.npmjs.com/package/package)
[![Node Version](https://img.shields.io/node/v/package.svg)](https://nodejs.org)

<!-- ライセンスとドキュメント -->
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Documentation](https://img.shields.io/badge/docs-available-brightgreen.svg)](https://docs.example.com)

<!-- コミュニティ -->
[![GitHub Stars](https://img.shields.io/github/stars/user/repo.svg?style=social)](https://github.com/user/repo/stargazers)
[![Discord](https://img.shields.io/discord/123456789.svg)](https://discord.gg/invite)

> プロジェクトの説明
```

---

## リソース

### バッジジェネレーター

- [Shields.io](https://shields.io) - カスタマイズ可能なバッジ
- [Badge Generator](https://badgen.net) - 軽量な代替
- [Simple Badges](https://github.com/badges/shields) - GitHubバッジ

### アイコンとロゴ

- [Simple Icons](https://simpleicons.org) - ブランドアイコン
- [Font Awesome](https://fontawesome.com) - 汎用アイコン
- [Devicons](https://devicon.dev) - 技術アイコン

### ツール

- [Badgen](https://badgen.net) - 高速バッジサービス
- [Version Badge](https://badge.fury.io) - パッケージバージョン
- [For the Badge](https://forthebadge.com) - ユーモラスなバッジ
