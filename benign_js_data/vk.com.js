<script type="text/javascript">
<!--
/*web_vitals_polyfill*/(function(){"use strict";var e,t,n,i,r,o,a,c,u,s,f,p;function l(){}return r={passive:!0,capture:!0},o=new Date,a=function n(){i=[],t=-1,e=null,f(addEventListener)},c=function i(r,o){e||(e=o,t=r,n=new Date,f(removeEventListener),u())},u=function r(){if(t>=0&&t<n-o){var a={entryType:"first-input",name:e.type,target:e.target,cancelable:e.cancelable,startTime:e.timeStamp,processingStart:e.timeStamp+t};i.forEach((function(e){e(a)})),i=[]}},s=function e(t){if(t.cancelable){var n=(t.timeStamp>1e12?new Date:performance.now())-t.timeStamp;"pointerdown"==t.type?(function(e,t){var n=function n(){c(e,t),o()},i=function e(){o()},o=function e(){removeEventListener("pointerup",n,r),removeEventListener("pointercancel",i,r)};addEventListener("pointerup",n,r),addEventListener("pointercancel",i,r)})(n,t):c(n,t)}},f=function e(t){["mousedown","keydown","touchstart","pointerdown"].forEach((function(e){return t(e,s,r)}))},p="hidden"===document.visibilityState?0:1/0,addEventListener("visibilitychange",(function e(t){"hidden"===document.visibilityState&&(p=t.timeStamp,removeEventListener("visibilitychange",e,!0))}),!0),a(),!void(self.webVitals={firstInputPolyfill:function e(t){i.push(t),u()},resetFirstInputPolyfill:a,get firstHiddenTime(){return p}}),l})()
//-->
</script>