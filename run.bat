@echo off

echo "1. 清理旧文件并编译..."
# 增加 --gc 参数清理未使用的缓存，增加 --cleanDestinationDir 确保目录干净
hugo --gc --cleanDestinationDir

echo "2. 初始化新增文件.."
git add .

echo "3. 提交文件到本地..."
git commit -m "清理冗余文件并更新内容"

echo "5. 推送到远程仓库....."
git push -u origin main

echo "6. 完成"
pause