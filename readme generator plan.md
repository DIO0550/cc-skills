# README 生成スキル 実装計画

## プロジェクト概要

GitHub プロジェクト用の高品質な README.md を構造化して生成するスキルを作成します。
初心者の学習用として、**全てのリソースタイプ（scripts/references/assets）を含む完全版**を実装します。

---

## スキル仕様

### 基本情報

```yaml
name: readme-generator
description: GitHubプロジェクト用のREADME.mdを構造化して生成。プロジェクトドキュメント、README作成、ドキュメンテーション、オープンソースプロジェクト用に使用。
```

### 対応するユースケース

1. **新規プロジェクト**: ゼロから README を作成
2. **既存プロジェクト**: 既存の README を改善・構造化
3. **テンプレート提供**: プロジェクトタイプ別のテンプレート
4. **バッジ生成**: 自動的にバッジを提案・生成

---

## ディレクトリ構造

```
readme-generator/
├── SKILL.md                          # メインスキルファイル
├── LICENSE.txt                       # ライセンス情報
├── scripts/                          # 実行可能スクリプト
│   ├── generate_badges.py           # バッジURLを生成
│   ├── validate_readme.py           # README品質チェック
│   └── analyze_project.py           # プロジェクトファイルを分析して内容を推測
├── references/                       # リファレンスドキュメント
│   ├── sections-guide.md            # 各セクションの詳細ガイド
│   ├── badge-types.md               # バッジの種類と使い方
│   ├── best-practices.md            # README作成のベストプラクティス
│   └── examples.md                  # 良いREADMEの実例
└── assets/                           # テンプレートファイル
    ├── templates/
    │   ├── basic.md                 # 基本テンプレート
    │   ├── library.md               # ライブラリプロジェクト用
    │   ├── webapp.md                # Webアプリケーション用
    │   └── cli-tool.md              # CLIツール用
    └── snippets/
        ├── installation.md          # インストール手順のスニペット
        ├── usage.md                 # 使用例のスニペット
        ├── contributing.md          # コントリビューションガイド
        └── license-sections.md      # ライセンスセクションの例
```

---

## 各ファイルの詳細仕様

### 1. SKILL.md（メインファイル）

**構成:**

```markdown
---
name: readme-generator
description: [上記の通り]
---

# README Generator

## 概要

このスキルを使用して GitHub プロジェクト用の README を生成

## ワークフロー

### ステップ 1: プロジェクトタイプの判定

ユーザーの入力またはプロジェクトファイルから以下を判定：

- ライブラリ/パッケージ
- Web アプリケーション
- CLI ツール
- その他

### ステップ 2: 必要情報の収集

以下の情報を収集（不足時はユーザーに質問）：

- プロジェクト名
- 説明
- 主な機能
- インストール方法
- 使用例

### ステップ 3: README 生成

1. 適切なテンプレートを選択（assets/templates/）
2. セクション詳細は references/sections-guide.md を参照
3. バッジが必要な場合は scripts/generate_badges.py を実行
4. 生成後、scripts/validate_readme.py で品質チェック

## 利用可能なリソース

### Scripts

- **generate_badges.py**: バッジ URL を生成
- **validate_readme.py**: README 品質チェック（必須セクション確認等）
- **analyze_project.py**: プロジェクト構造を分析

### References

- **sections-guide.md**: 各セクションの書き方詳細
- **badge-types.md**: 利用可能なバッジ一覧
- **best-practices.md**: README 作成のコツ
- **examples.md**: 優れた README の実例

### Assets

- **templates/**: プロジェクトタイプ別テンプレート
- **snippets/**: 再利用可能なセクションスニペット

## 使用パターン

[具体的な使用例]
```

**サイズ目標**: 300-400 行

---

### 2. scripts/generate_badges.py

**機能:**

- プロジェクト情報からバッジの Markdown を生成
- 対応バッジ: ビルドステータス、カバレッジ、バージョン、ライセンス、ダウンロード数

**入力例:**

```python
{
    "project_name": "my-awesome-lib",
    "language": "python",
    "license": "MIT",
    "ci_service": "github-actions"
}
```

**出力例:**

```markdown
![Build Status](https://github.com/user/my-awesome-lib/workflows/CI/badge.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/pypi/pyversions/my-awesome-lib.svg)
```

**実装方針:**

- shields.io の URL 生成ロジック
- 言語別の適切なバッジを選択
- JSON またはコマンドライン引数で実行可能

---

### 3. scripts/validate_readme.py

**機能:**

- README.md の品質をチェック
- 必須セクションの存在確認
- リンク切れチェック（オプション）
- 文字数や構造の検証

**チェック項目:**

- [ ] タイトル（H1）が存在
- [ ] 説明セクションがある
- [ ] インストール手順がある
- [ ] 使用例がある
- [ ] 各セクションが空でない
- [ ] コードブロックが正しく閉じられている

**出力:**

```
✅ タイトルが存在します
✅ 説明セクションが存在します
⚠️  使用例が短すぎる可能性があります（50文字以下）
❌ ライセンスセクションが見つかりません
```

---

### 4. scripts/analyze_project.py

**機能:**

- プロジェクトディレクトリを分析
- package.json、setup.py、Cargo.toml 等から情報抽出
- プロジェクトタイプを推測

**分析内容:**

- プログラミング言語（ファイル拡張子から）
- 依存関係管理ファイルの有無
- テストフレームワーク
- CI 設定ファイル

**出力例:**

```json
{
  "language": "python",
  "project_type": "library",
  "has_tests": true,
  "ci_service": "github-actions",
  "dependencies_file": "requirements.txt"
}
```

---

### 5. references/sections-guide.md

**内容:**

各セクションの詳細ガイド（15-20 セクション）：

1. **Project Title & Badges**

   - タイトルの書き方
   - 適切なバッジの選択

2. **Description**

   - 1-2 文の簡潔な説明
   - 「何を解決するか」を明確に

3. **Table of Contents**

   - いつ含めるべきか（長い README の場合）
   - 自動生成ツールの紹介

4. **Installation**

   - OS 別の手順
   - 前提条件
   - トラブルシューティング

5. **Usage**
   - 基本的な使用例
   - よくあるユースケース
   - コードサンプル

[... 他のセクション]

**サイズ**: 200-300 行

---

### 6. references/badge-types.md

**内容:**

利用可能なバッジの完全リスト：

- **ビルド/CI**: GitHub Actions, Travis CI, CircleCI
- **カバレッジ**: Codecov, Coveralls
- **バージョン**: npm, PyPI, Crates.io
- **ライセンス**: MIT, Apache, GPL
- **ダウンロード**: npm downloads, PyPI downloads
- **品質**: Code Climate, Codacy
- **コミュニティ**: Stars, Forks, Contributors

各バッジについて：

- 使用タイミング
- URL 生成方法
- カスタマイズオプション

**サイズ**: 150-200 行

---

### 7. references/best-practices.md

**内容:**

README 作成のベストプラクティス：

1. **構造**

   - 逆ピラミッド形式（重要な情報を上に）
   - セクション分けの基準

2. **文体**

   - 簡潔で明確に
   - 専門用語の適切な使用
   - 国際化を意識

3. **ビジュアル**

   - スクリーンショットの使用
   - GIF アニメーション
   - 図表の配置

4. **メンテナンス**

   - 最新情報の維持
   - バージョン情報の更新

5. **アクセシビリティ**
   - 画像の alt text
   - 明確なリンクテキスト

**サイズ**: 150-200 行

---

### 8. references/examples.md

**内容:**

優れた README の実例とその分析：

各例について：

- プロジェクト名と URL
- 優れている点
- 参考にすべき構造
- 使用されている技法

例：

- **React**: 明確な構造、豊富なリンク
- **Vue.js**: 多言語対応、視覚的に魅力的
- **Rust**: 詳細なドキュメント、例が豊富

**サイズ**: 100-150 行

---

### 9. assets/templates/basic.md

**内容:**

基本的なプロジェクト用のテンプレート：

```markdown
# [Project Name]

[Badges will be inserted here]

## Description

[Brief 1-2 sentence description]

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

[Installation instructions]

## Usage

[Basic usage example]

## Contributing

[Contribution guidelines]

## License

[License information]
```

---

### 10. assets/templates/library.md

**内容:**

ライブラリ/パッケージ用の詳細テンプレート：

追加セクション：

- API Reference
- Examples
- Requirements
- Development
- Testing

---

### 11. assets/templates/webapp.md

**内容:**

Web アプリケーション用テンプレート：

追加セクション：

- Demo
- Screenshots
- Deployment
- Environment Variables
- Architecture

---

### 12. assets/templates/cli-tool.md

**内容:**

CLI ツール用テンプレート：

追加セクション：

- Commands
- Options
- Configuration
- Examples

---

### 13. assets/snippets/installation.md

**内容:**

よく使うインストール手順のスニペット集：

- npm/yarn
- pip/pipenv
- cargo
- go get
- apt/brew
- Docker
- ソースからビルド

---

### 14. assets/snippets/usage.md

**内容:**

使用例のスニペット：

- 基本的なインポート
- 簡単な例
- 設定ファイルの例
- CLI 実行例

---

### 15. assets/snippets/contributing.md

**内容:**

コントリビューションガイドのテンプレート：

- Issue 報告方法
- Pull Request 手順
- コーディング規約
- 開発環境セットアップ

---

### 16. assets/snippets/license-sections.md

**内容:**

主要ライセンスの README セクション：

- MIT
- Apache 2.0
- GPL v3
- BSD

---

## 実装順序

### フェーズ 1: 基本構造（30 分）

1. ディレクトリ構造作成
2. SKILL.md の骨組み作成
3. LICENSE.txt 追加

### フェーズ 2: テンプレート作成（45 分）

4. assets/templates/の 4 ファイル作成
5. assets/snippets/の 4 ファイル作成

### フェーズ 3: リファレンス作成（60 分）

6. references/sections-guide.md
7. references/badge-types.md
8. references/best-practices.md
9. references/examples.md

### フェーズ 4: スクリプト実装（60 分）

10. scripts/generate_badges.py
11. scripts/validate_readme.py
12. scripts/analyze_project.py

### フェーズ 5: SKILL.md 完成（30 分）

13. SKILL.md の詳細記述
14. 各リソースへの適切な参照を追加

### フェーズ 6: テスト＆検証（30 分）

15. 各スクリプトの動作確認
16. SKILL.md の読みやすさ確認
17. package_skill.py で検証

**合計予想時間**: 約 4 時間

---

## 学習ポイント

このプロジェクトを通じて以下を学べます：

✅ **SKILL.md の書き方**

- フロントマター設定
- ワークフロー記述
- リソース参照方法

✅ **Scripts の活用**

- Python スクリプトの作成
- 入出力の設計
- エラーハンドリング

✅ **References の整理**

- 情報の階層化
- プログレッシブディスクロージャー
- ドキュメント分割の判断

✅ **Assets の管理**

- テンプレートの設計
- 再利用可能なスニペット作成
- プロジェクトタイプ別の最適化

✅ **スキル全体の設計**

- 各リソースの役割分担
- ユーザー体験の設計
- メンテナンス性の確保

---

## 次のステップ

この計画で進めますか？
それとも、何か調整したい部分はありますか？

調整案：

- もっとシンプルにする（一部リソースを削減）
- より高度にする（追加機能を含める）
- 特定の部分に注力する（例：スクリプトだけ充実させる）

準備ができたら、実装を開始しましょう！🚀
