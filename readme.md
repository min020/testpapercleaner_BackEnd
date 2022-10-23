# 시험지 Cleaner
시험지 Cleaner BackEnd

## 구현내용
- FrontEnd에서 사용자가 첨부파일로 입력한 이미지를 `POST Method`로 전달받음
- 전달받은 이미지를 딥러닝 모델에 입력으로 넣어 복원된 시험지 생성
- 생성된 이미지들을 zip 파일 형태로 만들어 aws s3에 업로드
- zip 파일의 이름을 FrontEnd에서 전달받은 uuid로 설정하여 고유의 다운로드 링크 생성
