'use strict';

const DEVTOOLS_RTT_ADJUSTMENT_FACTOR = 3.75;
const DEVTOOLS_THROUGHPUT_ADJUSTMENT_FACTOR = 0.9;

const throttling = {
    DEVTOOLS_RTT_ADJUSTMENT_FACTOR,
    DEVTOOLS_THROUGHPUT_ADJUSTMENT_FACTOR,
    mobileSlow4G: {
        rttMs: 150,
        throughputKbps: 1.6 * 1024,
        requestLatencyMs: 150 * DEVTOOLS_RTT_ADJUSTMENT_FACTOR,
        downloadThroughputKbps: 1.6 * 1024 * DEVTOOLS_THROUGHPUT_ADJUSTMENT_FACTOR,
        uploadThroughputKbps: 750 * DEVTOOLS_THROUGHPUT_ADJUSTMENT_FACTOR,
        cpuSlowdownMultiplier: 4,
    },
};

const settings = {
    output: 'json',
    maxWaitForLoad: 45 * 1000,
    auditMode: false,
    gatherMode: false,
    disableStorageReset: false,
    disableDeviceEmulation: true,
    emulatedFormFactor: 'desktop',
    locale: 'en-US',
    blockedUrlPatterns: null,
    additionalTraceCategories: null,
    extraHeaders: null,
    onlyAudits: null,
    onlyCategories: null,
    skipAudits: null
}

const passes = [{
    passName: 'defaultPass',
    recordTrace: true,
    useThrottling: true,
    pauseAfterLoadMs: 1000,
    networkQuietThresholdMs: 1000,
    cpuQuietThresholdMs: 1000,
    gatherers: [
        'dobetterweb/domstats'
    ]
}]

const audits = [
    "bootup-time",
    "metrics/first-contentful-paint",
    "metrics/first-cpu-idle",
    "metrics/first-meaningful-paint",
    "metrics/interactive",
    "metrics/speed-index",
    "network-requests",
    "time-to-first-byte",
    "byte-efficiency/total-byte-weight",
    "dobetterweb/dom-size"
]

module.exports = {
    settings: settings,
    passes: passes,
    audits: audits
};