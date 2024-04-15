import React from 'react';
import styles from './headersearch.module.css';

export function HeaderSearch() {
  return (
    <div className={styles.wrapper}>
      <button className={styles.button}>
        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 30 30" fill="none">
          <path fillRule="evenodd" clipRule="evenodd" d="M13.75 0.3125C7.01903 0.3125 1.5625 5.76903 1.5625 12.5C1.5625 19.231 7.01903 24.6875 13.75 24.6875C20.481 24.6875 25.9375 19.231 25.9375 12.5C25.9375 5.76903 20.481 0.3125 13.75 0.3125ZM3.4375 12.5C3.4375 6.80456 8.05456 2.1875 13.75 2.1875C19.4454 2.1875 24.0625 6.80456 24.0625 12.5C24.0625 18.1954 19.4454 22.8125 13.75 22.8125C8.05456 22.8125 3.4375 18.1954 3.4375 12.5Z" fill="#3D3D3D"/>
          <path d="M24.413 21.8372C24.0469 21.4711 23.4533 21.4711 23.0872 21.8372C22.7211 22.2033 22.7211 22.7969 23.0872 23.163L28.087 28.163C28.4531 28.5291 29.0467 28.5291 29.4129 28.163C29.779 27.7969 29.779 27.2033 29.4129 26.8371L24.413 21.8372Z" fill="#3D3D3D"/>
        </svg>
      </button>
      <input className={styles.input} type="text" placeholder='специальность' />
    </div>
  );
}
