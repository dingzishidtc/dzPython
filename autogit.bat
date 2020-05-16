rem CODE BY t0nsha 
git add *
git commit -m "%date:~0,10% %time:~0,-3% 增加的测试文件"
git push
echo "%date:~0,10% %time:~0,-3% 变更文件已提交至git远程仓库" >>gitlog.txt