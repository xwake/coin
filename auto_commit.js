//gitĿ¼���½�index.js
const child_process = require("child_process");
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
//��&&���Ӷ���CMD����
const cmd = 'git add --all :/ && git commit -m "update" && git push origin master';
execCMD(cmd);