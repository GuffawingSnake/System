module.exports = {
  root: true,
  env: {
    node: true
  },
  extends: [
    'plugin:vue/essential',
    '@vue/standard'
  ],
  parserOptions: {
    parser: 'babel-eslint'
  },
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    // 允许函数括号前不加空格
    'space-before-function-paren': ['error', {
      anonymous: 'never',
      named: 'never',
      asyncArrow: 'always'
    }],
    // 允许尾随空格
    'no-trailing-spaces': ['error', {
      skipBlankLines: true,
      ignoreComments: true
    }],
    // 允许使用下划线命名
    'camelcase': ['error', {
      properties: 'never',
      ignoreDestructuring: true,
      allow: ['^UNSAFE_', '^unused_', '^visitor_']
    }]
  }
} 
