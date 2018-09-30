//gitĿ¼���½�index.js
const child_process = require("child_process");
//��&&���Ӷ���CMD����
const cmd = 'git add --all :/ && git commit -m "update" && git push origin master';

var schedule = require('node-schedule');

//����һ��ִ��cmd�ĺ���
const execCMD = function(cmd){
  child_process.exec(cmd, function(error, stdout, stderr) {
    if(error) {
        console.error('error: ' + error);
        return;
    }
    console.log('stdout: ' + stdout);
    console.log('stderr: ' + stderr);
  })
}


function scheduleExecute(){
    schedule.scheduleJob('0 */5 * * * *', function(){
        console.log('scheduleExecute: ' + new Date());
		execCMD(cmd);
    }); 
}

scheduleExecute();



/*
https://zj-john.github.io/projects/cjfcgrwnu008pa8f0jy7s6s3j.html



node-schedule
	https://www.jianshu.com/p/f787593071e1
	http://www.cnblogs.com/zhongweiv/p/node_schedule.html
	http://cron.qqe2.com/ 
	http://wiki.jikexueyuan.com/project/nodejs-guide/module-path.html ·��

LINUX
export NODE_PATH=/usr/local/lib/node_modules/  

WINDOWS
�������� NODE_PATH = /DIR/node_modules


*/


