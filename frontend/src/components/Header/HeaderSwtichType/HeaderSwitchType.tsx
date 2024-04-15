import React from 'react';
import styles from './headerswitchtype.module.css';

export function HeaderSwitchType() {
  return (
    <div className={styles.wrapper}>
      <button className={`${styles.button} ${styles.active}`}>вакансии</button>
      <button className={styles.button}>навыки</button>
    </div>
  );
}
