const lighthouse = require('lighthouse');
const chromeLauncher = require('chrome-launcher');
const config = require('./config')

const opts = {
    chromeFlags: ['--show-paint-rects']
};

const CSR = 'csr'
const SSR = 'ssr'
const CSR_URL = 'https://client-side-app.herokuapp.com/'
const SSR_URL = 'https://server-side-app.herokuapp.com/'
const NUMBER_OF_INTERACTIONS = 100

function launchChromeAndRunLighthouse(url, opts, config = null) {
    return chromeLauncher.launch({
        chromeFlags: opts.chromeFlags
    }).then(chrome => {
        opts.port = chrome.port;
        return lighthouse(url, opts, config).then(results => {
            return chrome.kill().then(() => results.lhr)
        });
    });
}

var interactions = NUMBER_OF_INTERACTIONS
if(process.argv.length >= 2) {
    interactions = process.argv.slice(2);
} 

for(var i; i<interactions; i++) {
    launchChromeAndRunLighthouse(SSR_URL, opts, config)
        .then(results => {
            console.log(results)
        });

    launchChromeAndRunLighthouse(CSR_URL, opts, config)
        .then(results => {
            console.log(results)
        });
}
