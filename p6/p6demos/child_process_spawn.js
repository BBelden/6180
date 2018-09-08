
const spawn = require('child_process').spawn;

var bc = spawn('/usr/bin/bc', ['-l']);
var output = '';

bc.stdout.on('data', function(data) {
    output += data.toString();
});

bc.stdout.on('end', function() {
    console.log(output);
});

bc.stdin.write("4*5" + '\n');
bc.stdin.write("8/3" + '\n');
bc.stdin.end();

