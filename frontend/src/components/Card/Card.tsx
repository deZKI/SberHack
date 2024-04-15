import React from 'react';
import styles from './card.module.css';
import Avatar from '../../assets/images/avatar-user.png';

export function Card() {
  return (
    <div className={styles.container}>
      <div className={styles.main}>
        <div className={styles.avatar}>
          <img className={styles.avatarImage} src={Avatar} alt="avatar" />
        </div>
        <div className={styles.information}>
          <div className={styles.informationIdentity}>
            <h4 className={styles.informationIdentityFullname}>Иванов Иван Иванович</h4>
            <h5 className={styles.informationIdentityPosition}>Главный разработчик</h5>
          </div>
          <div className={styles.informationSkills}>
            <ul className={styles.informationSkillsList}>
              <li className={styles.informationSkillsItem}>саморазвитие</li>
              <li className={styles.informationSkillsItem}>java-разработка</li>
            </ul>
          </div>
        </div>
        <button className={styles.button}>
          <svg xmlns="http://www.w3.org/2000/svg" width="84" height="85" viewBox="0 0 84 85" fill="none">
            <path d="M33.8332 22.0833L41.032 29.2182C46.7728 34.9081 49.6433 37.753 50.0853 41.2206C50.1936 42.0701 50.1936 42.9299 50.0853 43.7794C49.6433 47.247 46.7729 50.0919 41.032 55.7818L33.8332 62.9167M41.9998 1.66667C64.5515 1.66667 82.8332 19.9484 82.8332 42.5C82.8332 65.0516 64.5515 83.3333 41.9998 83.3333C19.4482 83.3333 1.1665 65.0516 1.1665 42.5C1.1665 19.9484 19.4482 1.66667 41.9998 1.66667Z" strokeWidth="1.5" strokeLinecap="round"/>
          </svg>
        </button>
      </div>
      <div className={styles.optional}>
        <div className={styles.divider}></div>
      </div>
    </div>
  );
}
