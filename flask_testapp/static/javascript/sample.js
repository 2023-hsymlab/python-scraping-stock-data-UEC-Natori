window.onload = function() {
    var e = document.getElementById('test');
    var changeColor01 = function() {
        var e = document.getElementById('test');
        e.style.color = 'red';
        console.log("書き換えテスト")
    }
    var changeColor02 = function() {
        var e = document.getElementById('test');
        e.style.color = 'green';
        console.log("書き換えテスト")
    }
    var changeColor03 = function() {
        var e = document.getElementById('test');
        e.style.color = 'blue';
        console.log("書き換えテスト")
    }

    function sleep(waitMsec) {
        var startMsec = new Date();
       
        // 指定ミリ秒間だけループさせる（CPUは常にビジー状態）
        while (new Date() - startMsec < waitMsec);
    }
     


        e.style.color = 'red';
        sleep(500);
        e.style.color = 'blue';
        sleep(500);
        e.style.color = 'green';
        sleep(500);

    
    setTimeout(changeColor02, 2000);
}
