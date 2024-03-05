# 変数の命名について
[The Art Of Readable Code](https://mcusoft.files.wordpress.com/2015/04/the-art-of-readable-code.pdf)  
Part One: PACKING INFORMATION INTO NAMESのあたり

以下のようなデータ構造の時、ユーザーが所属するクラブを出力するコードを考える

```python
# pythonでの例(c++で考える場合もこのようなマップと配列に適宜読み替えてください)
# clubs: クラブとメンバーのmap
clubs = {
	"club1": ["user1", "user2"],
	"club2": ["user2", "user3", "user4"],
	"club3": ["user1", "user3", "user4"],
	"club4": ["user1", "user3", "user4"],
}

# users: ユーザのリスト
users = ["user1", "user2", "user3", "user4", "user5"]
```

```php

$clubs = array(
	"club1" => array("user1", "user2"),
	"club2" => array("user2", "user3", "user4"),
	"club3" => array("user1", "user3", "user4"),
	"club4" => array("user1", "user3", "user4")
);

$users = array("user1", "user2", "user3", "user4", "user5");
```

### Question1. 実装してみる(どの言語でも大丈夫です) 5分くらい
function(clubs, users) -> {user: club}  

引数1: clubs, 引数2: users　　
return {key: user, value: list["club"]} の辞書、連想配列、マップなどを返す関数  
```
↓こんな感じの帰り値
{
	"user1": ["club1", "club3", "club4"],
	"user2": ["club1", "club2"],
}
```

### Question2. 以下のコードにバグはありますか？ 1分くらい
---
(※ indexの変数名について考えたいので、総当たりで探すことを考える)



```c++
// c++
for (int i = 0; i < clubs.size(); i++) {
	for (int j = 0; j < clubs[i].members.size(); j++) {
		for (int k = 0; k < users.size(); k++) {
			if (clubs[i].members[k] == users[j]) {
				cout << "user[" << j << "] is in club[" << i << "]" << endl;
			}
		}
	}
}
```

```python
# python
for i in range(len(clubs)):
	for j in range(len(clubs[i].members)):
		for k in range(len(users)):
			if clubs[i].members[k] == users[j]:
				print(f"user[{j}] is in club[{i}]")
```



`i` は `clubs` のインデックス、`j` は `clubs[i].members` のインデックス、`k` は `users` のインデックスを表している。
このようなコードがあったとき、`i`, `j`, `k` は何を表しているのかがわかりにくい。

### indexの命名を改訂
---
i, j, k は何を表しているのかを明確にするために、indexの名前を以下のように変更  
```
i: club_index
j: member_index
k: user_index
```

### Question3. 以下のコードにバグはありますか？ 1分くらい

```c++
// c++
for (int club_index = 0; club_index < clubs.size(); club_index++) {
	for (int member_index = 0; member_index < clubs[club_index].members.size(); member_index++) {
		for (int user_index = 0; user_index < users.size(); user_index++) {
			if (clubs[club_index].members[user_index] == users[member_index]) {
				cout << "user[" << member_index << "] is in club[" << club_index << "]" << endl;
			}
		}
	}
}
```

```python
# python
for club_index in range(len(clubs)):
	for member_index in range(len(clubs[club_index].members)):
		for user_index in range(len(users)):
			if clubs[club_index].members[user_index] == users[member_index]:
				print(f"user[{member_index}] is in club[{club_index}]")
```



### indexが長いとちょっと見づらい...さらにindexの命名を改訂
indexの名前を以下のように変更  
```
i: club_i
j: member_i
k: user_i
```

### Question4. 以下のコードにバグはありますか？ 1分くらい

```c++
// c++
for (int club_i = 0; club_i < clubs.size(); club_i++) {
	for (int member_i = 0; member_i < clubs[club_i].members.size(); member_i++) {
		for (int user_i = 0; user_i < users.size(); user_i++) {
			if (clubs[club_i].members[user_i] == users[member_i]) {
				cout << "user[" << member_i << "] is in club[" << club_i << "]" << endl;
			}
		}
	}
}
```

```python
# python
for club_i in range(len(clubs)):
	for member_i in range(len(clubs[club_i].members)):
		for user_i in range(len(users)):
			if clubs[club_i].members[user_i] == users[member_i]:
				print(f"user[{member_i}] is in club[{club_i}]")
```

少し見やすくなったけど

### これくらい短いコードだったら、もう少し短くても良さそう
indexの名前を以下のように変更  
```
i: c_i
j: m_i
k: u_i
```

### Question5. 以下のコードにバグはありますか？ 1分くらい


```c++
// c++
for (int c_i = 0; c_i < clubs.size(); c_i++) {
	for (int m_i = 0; m_i < clubs[c_i].members.size(); m_i++) {
		for (int u_i = 0; u_i < users.size(); u_i++) {
			if (clubs[c_i].members[u_i] == users[m_i]) {
				cout << "user[" << m_i << "] is in club[" << c_i << "]" << endl;
			}
		}
	}
}
```

```python
# python
for c_i in range(len(clubs)):
	for m_i in range(len(clubs[c_i].members)):
		for u_i in range(len(users)):
			if clubs[c_i].members[u_i] == users[m_i]:
				print(f"user[{m_i}] is in club[{c_i}]")
```

# indexの変数名に限らず、可読性を考慮する時の変数の命名で大切なこと
1. `Code should be written to minimize the time it would take for someone else to understand it.`  
→ 他の人が理解するのにかかる時間を最小限にするためにコードを書くべき

## 長い変数名 vs 短い変数名
- 長い変数名
  - メリット: 変数の役割がわかりやすい
    - 例: newNavigationControllerWrappingViewControllerForDataSourceOfClass　→　役割はわかりやすいが、長すぎて読みにくい
  - デメリット: コードが長くなる、読みにくくなる
- 短い変数名
  - メリット: コードが短くなる
  - デメリット: 変数の役割がわかりにくい
    - 例: d  →  日付？距離？データ？

## どちらを選ぶべきか
変数のスコープ(使われている範囲)によって決める
- 短い変数名: スコープ、が短い変数
- 長い変数名: スコープが長い変数

いずれも、どのようにしたら他の人が読んだ時に最速でコードが理解できるようになるか、を考えることが大切  
→　コードが短ければ、短いほど良いというわけではない

### 例: リスト内包表記を使ったコード(python)
```python
matches = [(m_i, c_i) for c_i, club in enumerate(clubs) for m_i, member in enumerate(club.members) if member in users]
for m_i, c_i in matches:
	print(f"user[{m_i}] is in club[{c_i}]")
```

記述量は減ったが、リスト内包括内でfor分をネストしているため、読みにくい


# 時間が余ったら
1. 上記コードのネストを減らす方法を考えてみる
2. 簡単はアルゴリズムの問題を解いてみる

### 2-1
あるリストから、2つの数字を足して、特定の数字になる組み合わせがあれば返す関数を実装してみる  

例: [11, 2, 5, 9, 10, 31] というリストがある時、この中から2つの数字を足して、12になるペアがあるかどうかを判定する
この場合、2 + 10 = 12 なので、Trueを返す

```python
# python
from typing import List, Optional, Tuple

# [11, 2, 5, 9, 10, 31], 12 -> (2, 10)
def get_pair_with_sum(List[int], sum: int) -> Optional[Tuple[int, int]]:
	# your code here
	...

lst = [11, 2, 5, 9, 10, 31]
target = 12
print(get_pair_with_sum(lst, target))  # (2, 10)
```

```php
// php
function get_pair_with_sum(array $list, int $sum): ?array {
	// your code here
	...
}

$lst = [11, 2, 5, 9, 10, 31];
$target = 12;
print_r(get_pair_with_sum($lst, $target));  // [2, 10]
```





### 2-2
あるリストの中の２つの数字の合計が、それいがいの他の数字の合計と等しくなるようなペアがあれば返す関数を実装してみる
例: [11, 2, 5, 9, 10, 3] というリストがある時、この中から2つの数字を足して、それ以外の数字の合計と等しくなるペアを探す
11 + 9 = 2 + 5 + 10 + 3 なので、(11, 9)

```python
def get_pair_with_half_sum(List[int]) -> Optional[Tuple[int, int]]:
	# your code here
	...


lst = [11, 2, 5, 9, 10, 3]
print(get_pair_with_half_sum(lst))  # (11, 9)
```


```php

function get_pair_with_half_sum(array $list): ?array {
	// your code here
	...
}


$lst = [11, 2, 5, 9, 10, 3];
print_r(get_pair_with_half_sum($lst));  // [11, 9]
```