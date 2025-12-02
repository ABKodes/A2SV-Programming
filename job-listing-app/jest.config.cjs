module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'jest-environment-jsdom',
  transform: {
    "^.+\\.tsx?$": ["ts-jest", {
      tsconfig: {
        jsx: "react-jsx",
        esModuleInterop: true  // <--- THIS FIXES THE ERROR
      }
    }]
  },
  moduleNameMapper: {
    // Handle CSS imports (CSS modules)
    '\\.(css|less|sass|scss)$': 'identity-obj-proxy',
    // Handle Image imports
    '\\.(gif|ttf|eot|svg|png)$': '<rootDir>/test/__mocks__/fileMock.js',
  },
  setupFilesAfterEnv: ['<rootDir>/jest.setup.ts'],
};