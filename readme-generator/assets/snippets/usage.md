# 使用方法スニペット

様々なプログラミング言語とフレームワークの一般的な使用パターンとコード例。

## 基本的なインポートパターン

### JavaScript (ES6)
```javascript
import { functionName } from 'package-name';
```

### JavaScript (CommonJS)
```javascript
const packageName = require('package-name');
```

### Python
```python
import package_name
from package_name import ClassName, function_name
```

### Rust
```rust
use package_name::module_name;
```

### Go
```go
import "github.com/username/package-name"
```

## クイックスタート例

### ライブラリ - 基本的な使い方
```markdown
## クイックスタート

```言語
import package_name

# インスタンスを作成
instance = package_name.ClassName()

# メソッドを使用
result = instance.method_name()
print(result)  # 出力: 期待される結果
```
```

### CLIツール - 基本的な使い方
```markdown
## クイックスタート

```bash
# 基本コマンド
tool-name command --option value

# ヘルプを取得
tool-name --help

# 一般的なワークフロー
tool-name init my-project
cd my-project
tool-name build
tool-name run
```
```

## API例

### REST APIクライアント
```javascript
// GETリクエスト
const response = await api.get('/users');
console.log(response.data);

// POSTリクエスト
const newUser = await api.post('/users', {
  name: 'John Doe',
  email: 'john@example.com'
});

// PUTリクエスト
const updated = await api.put('/users/1', {
  name: 'Jane Doe'
});

// DELETEリクエスト
await api.delete('/users/1');
```

### データベース接続
```python
# データベースに接続
db = Database.connect(
    host='localhost',
    port=5432,
    database='mydb',
    user='user',
    password='password'
)

# クエリ
results = db.query('SELECT * FROM users WHERE active = ?', [True])

# 挿入
db.execute('INSERT INTO users (name, email) VALUES (?, ?)', 
           ['John Doe', 'john@example.com'])

# 接続を閉じる
db.close()
```

## 設定例

### JSON設定
```json
{
  "name": "my-project",
  "version": "1.0.0",
  "config": {
    "option1": "value1",
    "option2": true,
    "option3": 42
  }
}
```

### YAML設定
```yaml
name: my-project
version: 1.0.0

config:
  option1: value1
  option2: true
  option3: 42

features:
  - feature1
  - feature2
```

### 環境変数
```bash
# .envファイル
API_KEY=your_api_key_here
DATABASE_URL=postgresql://localhost/mydb
DEBUG=true
PORT=3000
```

## 一般的なユースケース

### ユースケース1: 基本操作
```markdown
### 基本操作

作成、読み取り、更新、削除操作：

```言語
# 作成
item = api.create({
  name: 'Item 1',
  value: 100
});

# 読み取り
item = api.get(item.id);

# 更新
api.update(item.id, {
  value: 200
});

# 削除
api.delete(item.id);
```
```

### ユースケース2: エラーハンドリング
```markdown
### エラーハンドリング

適切なエラーハンドリングパターン：

```言語
try {
  const result = await api.riskyOperation();
  console.log('成功:', result);
} catch (error) {
  if (error instanceof APIError) {
    console.error('APIエラー:', error.message);
    console.error('ステータス:', error.statusCode);
  } else if (error instanceof ValidationError) {
    console.error('検証失敗:', error.errors);
  } else {
    console.error('予期しないエラー:', error);
  }
}
```
```

## テスト例

### ユニットテスト
```javascript
describe('MyClass', () => {
  test('正しい値を返すべき', () => {
    const instance = new MyClass();
    const result = instance.method();
    expect(result).toBe(expectedValue);
  });
  
  test('エラーを処理すべき', () => {
    const instance = new MyClass();
    expect(() => instance.invalidMethod()).toThrow();
  });
});
```

## Docker使用方法

### 基本的なDockerコマンド
```bash
# イメージをビルド
docker build -t myapp:latest .

# コンテナを実行
docker run -d -p 8080:8080 myapp:latest

# ログを表示
docker logs container-id

# コンテナを停止
docker stop container-id
```

## パフォーマンスのヒント

```markdown
## パフォーマンス最適化

### キャッシング
```言語
// キャッシングを使用してパフォーマンスを向上
const cache = new Cache();

async function getData(key) {
  // まずキャッシュをチェック
  const cached = cache.get(key);
  if (cached) return cached;
  
  // キャッシュにない場合はフェッチ
  const data = await fetchData(key);
  cache.set(key, data, { ttl: 3600 });
  return data;
}
```
```

## セキュリティのベストプラクティス

```markdown
## セキュリティ

### 入力検証
```言語
function validateInput(data) {
  // ユーザー入力をサニタイズ
  const sanitized = sanitize(data);
  
  // スキーマに対して検証
  const { error, value } = schema.validate(sanitized);
  if (error) {
    throw new ValidationError(error.message);
  }
  
  return value;
}
```

### 認証
```言語
// リクエストを認証
const token = generateToken(user);

// リクエストでトークンを使用
const response = await api.get('/protected', {
  headers: {
    'Authorization': `Bearer ${token}`
  }
});
```
```
