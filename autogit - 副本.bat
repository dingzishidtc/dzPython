rem CODE BY t0nsha 
git add *
git commit -m "%date:~0,10% %time:~0,-3% ���ӵĲ����ļ�"
set /p msg=Username for 'https://github.com':

if %msg% == Y goto start
if %msg% == N goto stop

:start
dingzishidtc
goto end

:stop
git push
echo "%date:~0,10% %time:~0,-3% ����ļ����ύ��gitԶ�ֿ̲�" >>gitlog.txt