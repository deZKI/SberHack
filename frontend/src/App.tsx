import React from 'react';
import './main.global.css';
import {IInitialState, rootReducer} from "./store/reducer";
import {composeWithDevTools} from "redux-devtools-extension";
import {applyMiddleware, createStore} from "redux";
import thunk from "redux-thunk";
import {Provider, useSelector} from "react-redux";
import {Header} from "./shared/Header";
import {Content} from "./shared/Content";

const store = createStore(rootReducer, composeWithDevTools(
  applyMiddleware(thunk)
));

function AppComponent() {
  const startButtonClicked = useSelector<IInitialState, boolean>(state => state.startButtonClicked.startButtonClicked);

  return (
    <div className="container">
      <Header />
      <Content />
    </div>
  );
}

export const App = () => 
  <Provider store={store}>
    <AppComponent />
  </Provider>
;
