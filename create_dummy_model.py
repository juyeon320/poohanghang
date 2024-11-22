import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import os

# 더미 모델 생성
model = Sequential([
    Dense(10, activation='relu', input_shape=(5,)),  # 입력: 5개 특징, 은닉층: 10개 뉴런
    Dense(5, activation='relu'),  # 은닉층
    Dense(1, activation='sigmoid')  # 출력층
])

# 모델 컴파일
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 더미 모델 저장 경로
model_dir = os.path.join(os.getcwd(), 'capstone_design', 'models')
os.makedirs(model_dir, exist_ok=True)
MODEL_PATH = os.path.join(model_dir, 'models.h5')

# 더미 모델 저장
model.save(MODEL_PATH)
print(f"더미 모델이 {MODEL_PATH} 경로에 저장되었습니다.")
