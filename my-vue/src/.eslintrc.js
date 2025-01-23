module.exports = {
  root: true,
  env: {
    node: true
  },
  extends: [
    'plugin:vue/essential'
  ],
  parserOptions: {
    parser: 'babel-eslint'
  },
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'space-before-function-paren': 'off',
    'no-trailing-spaces': 'off',
    'camelcase': 'off',
    'indent': ['error', 2, {
      'SwitchCase': 1,
      'ignoredNodes': ['SwitchCase *']
    }],
    'quotes': ['error', 'single'],
    'semi': ['error', 'never']
  }
} 
