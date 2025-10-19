# インストール手順スニペット

各種パッケージマネージャーとプラットフォーム向けの一般的なインストール手順。

## Node.js / npm

### npm
```bash
npm install package-name
```

### npm (グローバル)
```bash
npm install -g package-name
```

### yarn
```bash
yarn add package-name
```

### pnpm
```bash
pnpm add package-name
```

## Python

### pip
```bash
pip install package-name
```

### pip (ユーザーインストール)
```bash
pip install --user package-name
```

### pipenv
```bash
pipenv install package-name
```

### poetry
```bash
poetry add package-name
```

### conda
```bash
conda install package-name
```

## Ruby

### gem
```bash
gem install package-name
```

### bundler
```ruby
# Gemfileに追加
gem 'package-name'
```

```bash
bundle install
```

## Rust

### cargo
```bash
cargo install package-name
```

## Go

### go install
```bash
go install github.com/username/package-name@latest
```

## システムパッケージマネージャー

### macOS (Homebrew)
```bash
brew install package-name
```

### Linux (apt)
```bash
sudo apt update
sudo apt install package-name
```

### Linux (yum/dnf)
```bash
sudo dnf install package-name
```

### Linux (snap)
```bash
sudo snap install package-name
```

### Windows (Chocolatey)
```bash
choco install package-name
```

### Windows (winget)
```bash
winget install package-name
```

## ソースからビルド

### 標準ビルド
```bash
git clone https://github.com/username/package-name.git
cd package-name
make
sudo make install
```

### CMake
```bash
git clone https://github.com/username/package-name.git
cd package-name
mkdir build && cd build
cmake ..
make
sudo make install
```

## Docker

### プルして実行
```bash
docker pull username/package-name
docker run -it username/package-name
```

### Docker Compose
```yaml
version: '3.8'
services:
  app:
    image: username/package-name:latest
    ports:
      - "8080:8080"
```

```bash
docker-compose up -d
```

## バイナリダウンロード

### Linux/macOS (curl)
```bash
curl -L https://github.com/username/package/releases/latest/download/package-linux -o package
chmod +x package
sudo mv package /usr/local/bin/
```

### Windows (PowerShell)
```powershell
Invoke-WebRequest -Uri "https://github.com/username/package/releases/latest/download/package.exe" -OutFile "package.exe"
```

## 前提条件セクションのテンプレート

### 最小限
```markdown
## 前提条件

- Node.js 18+ または Python 3.9+
```

### 標準
```markdown
## 前提条件

インストール前に以下を確認してください：

- **Node.js** 18.0以上
- **npm** 8.0以上（Node.jsに付属）
- **Git**（リポジトリのクローン用）
```

### 詳細
```markdown
## 前提条件

### 必須

- **Node.js** 18.0以上 - [ダウンロード](https://nodejs.org/)
- **npm** 8.0以上（Node.jsに付属）
- **PostgreSQL** 14+ - [ダウンロード](https://www.postgresql.org/download/)

### オプション

- **Redis** 6.0+（キャッシング用） - [ダウンロード](https://redis.io/download)
- **Docker**（コンテナ化デプロイ用） - [ダウンロード](https://www.docker.com/get-started)

### プラットフォーム固有の要件

**macOS:**
```bash
xcode-select --install
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install build-essential
```

**Windows:**
- Visual Studio Build Tools または Visual Studio Community Edition
```

## インストール確認

```markdown
## インストールの確認

インストール後、正しくインストールされたことを確認：

```bash
package-name --version
```

以下のような出力が表示されるはずです：
```
package-name v1.2.3
```

基本機能をテスト：
```bash
package-name test-command
```
```

## インストールのトラブルシューティング

```markdown
## トラブルシューティング

### よくあるインストールの問題

**問題: コマンドが見つかりません**

解決策: パッケージがPATHにあることを確認：
```bash
export PATH="$PATH:/path/to/package/bin"
```

**問題: 権限が拒否されました**

解決策: 適切な権限で実行：
```bash
sudo npm install -g package-name
# または
pip install --user package-name
```

**問題: バージョンの競合**

解決策: 仮想環境またはバージョンマネージャーを使用：
```bash
# Python
python -m venv venv
source venv/bin/activate

# Node.js (nvm)
nvm install 18
nvm use 18
```
```
