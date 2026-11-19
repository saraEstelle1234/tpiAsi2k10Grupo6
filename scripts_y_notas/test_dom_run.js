const fs = require('fs');
const vm = require('vm');

const html = fs.readFileSync('index.html', 'utf8');
const scriptMatch = html.match(/<script[\s\S]*?>([\s\S]*?)<\/script>/i);
const jsCode = scriptMatch[1];

// Mock basic DOM environment
const elements = {};
function createMockElement(id) {
  return {
    id: id,
    classList: {
      add: () => {},
      remove: () => {},
      toggle: () => {},
      contains: () => false
    },
    style: {},
    addEventListener: () => {},
    querySelectorAll: () => [],
    querySelector: () => null,
    getBoundingClientRect: () => ({ left: 0, top: 0, width: 50, height: 50 }),
    innerText: '',
    textContent: '',
    appendChild: () => {},
    innerHTML: ''
  };
}

const mockDoc = {
  getElementById: (id) => {
    if (!elements[id]) elements[id] = createMockElement(id);
    return elements[id];
  },
  querySelectorAll: (selector) => {
    return [createMockElement('mock-el')];
  },
  querySelector: (selector) => createMockElement('mock-el'),
  createElement: (tag) => createMockElement(tag),
  addEventListener: () => {},
  removeEventListener: () => {},
  fullscreenElement: null,
  documentElement: {
    requestFullscreen: () => Promise.resolve()
  },
  exitFullscreen: () => Promise.resolve()
};

const mockWindow = {
  document: mockDoc,
  addEventListener: () => {},
  removeEventListener: () => {},
  scrollTo: () => {},
  innerHeight: 900,
  innerWidth: 1400,
  setTimeout: setTimeout,
  clearTimeout: clearTimeout,
  setInterval: setInterval,
  clearInterval: clearInterval,
  console: console
};

const context = vm.createContext({
  window: mockWindow,
  document: mockDoc,
  console: console,
  setTimeout: setTimeout,
  clearTimeout: clearTimeout,
  navigator: { userAgent: 'node-test' },
  location: { href: 'http://localhost' }
});

try {
  vm.runInContext(jsCode, context);
  console.log("TEST PASSED: Script executed in mock DOM with ZERO runtime errors!");
} catch (err) {
  console.error("TEST FAILED: Runtime error in script:", err);
  process.exit(1);
}
