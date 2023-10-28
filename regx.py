# 'https://www.tiktok.com/@vantoan___/video/7246055282323868954'
# tiktok-x6y88p-DivItemContainerV2 e19c29qe8

let l = [];
let regex = /(^|.*)https:\/\/www.tiktok.com\/@(.*)\/video\/(.*|$)/;
document.getElementsByClassName('tiktok-x6y88p-DivItemContainerV2 e19c29qe8').forEach(i => {
    var a = i.querySelector('a').href;
    if(regex.test(a)) l.push(a);
});
console.log(l);
#var divs = document.querySelectorAll('div[class="DivItemContainerV2"]');
#console.log(divs)
#console.log(/(^|.*)-DivItemContainerV2(.*|$)/.test("tiktok-x6y88p-DivItemContainerV2 e19c29qe8"));
# let l = [];
# let regex = /(^|.*)-DivItemContainerV2(.*|$)/g
# const element = document.getElementById("app");
# # let d = document.documentElement.outerHTML.match(regex).forEach(i => {l.push(i.querySelector('a').href)});
# let d = document.documentElement.outerHTML.match(regex).forEach(i => console.log(i));
# console.log(d);

console.log(/(^|.*)https:\/\/www.tiktok.com\/@(.*)\/video\/(.*|$)/.test("https://www.tiktok.com/@vantoan___/video/7246055282323868954"));
console.log(/(^|.*)https:\/\/www.tiktok.com\/@(.*)\/video\/(.*|$)/.test("https://www.tiktok.com/"));

import re

txt = "https://www.tiktok.com/@vantoan___/video/7246055282323868954"
x = re.search("https://www.tiktok.com/", txt)