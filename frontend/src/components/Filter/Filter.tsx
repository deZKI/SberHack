import React from 'react';
import styles from './filter.module.css';
import { FilterIcon } from '../Icons/FilterIcon';

export function Filter() {
  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h4 className={styles.title}>фильтр</h4>
        <span className={styles.icon}><FilterIcon /></span>
      </div>
      <div className={styles.wrapper}>
        <input className={styles.filter} type="text" />
        <input className={styles.filter} type="text" />
        <input className={styles.filter} type="text" />
      </div>
      <button className={styles.button}>Добавить</button>
    </div>
  );
}
