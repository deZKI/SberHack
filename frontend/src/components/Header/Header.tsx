import React from "react";
import styles from './header.module.css';
import { HeaderSearch } from "./HeaderSearch";
import { HeaderSwitchType } from "./HeaderSwtichType";

export function Header() {
  return (
    <header className={styles.header}>
      <div className={styles.container}>
        <HeaderSearch />
        <HeaderSwitchType />
      </div>
    </header>
  );
}
