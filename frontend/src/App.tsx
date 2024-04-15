import React from 'react';
import './main.global.css';
import {rootReducer} from "./store/reducer";
import {composeWithDevTools} from "redux-devtools-extension";
import {applyMiddleware, createStore} from "redux";
import thunk from "redux-thunk";
import {Provider, useSelector} from "react-redux";
import { Header } from './components/Header';
import { Content } from './components/Content';

const store = createStore(rootReducer, composeWithDevTools(
  applyMiddleware(thunk)
));

function AppComponent() {
  return (
    <>
      <Header />
      <Content />
    </>
  );
}

export const App = () => 
  <Provider store={store}>
    <AppComponent />
  </Provider>
;
