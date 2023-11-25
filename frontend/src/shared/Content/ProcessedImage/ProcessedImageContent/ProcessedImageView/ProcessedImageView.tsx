import React from 'react';
import styles from './processedimageview.module.css';
import {useSelector} from "react-redux";
import {IInitialState} from "../../../../../store/reducer";

export function ProcessedImageView() {
  const uploadedImage = useSelector<IInitialState, string>(state => state.uploadedImage.uploadedImage);
  const processedImage = useSelector<IInitialState, string>(state => state.processedImage.processedImage);
  const switchOnOff = useSelector<IInitialState, boolean>(state => state.switcher.switcher);

  return (
    <div className={styles.container}>
      <img className={styles.image} src={switchOnOff ? uploadedImage : processedImage} alt="Processed image" />
    </div>
  );
}
