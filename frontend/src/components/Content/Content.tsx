import React from 'react';
import styles from './content.module.css';
import { Card } from '../Card';
import { Filter } from '../Filter';

export function Content() {
  return (
    <div className={styles.container}>
      <div className={styles.wrapper}>
        <div className={styles.cardWrapper}>
          {Array.from(Array(10).keys()).map(() => <Card />)}
        </div>
        <div className={styles.filterWrapper}>
          <Filter />
        </div>
      </div>
    </div>
  );
}
