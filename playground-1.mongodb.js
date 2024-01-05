// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use('tm-store');

// Create a new document in the collection.
db.getCollection('acc-links').insertOne({
  "name": "Google",
  "key": "google",
  "clientID": {
    "web": {
      "client_id": "235324461758-n9qs0f3kec5e8q8t2almq6edn0cjh704.apps.googleusercontent.com",
      "project_id": "tmstore-397006",
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://oauth2.googleapis.com/token",
      "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
      "client_secret": "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",
      "redirect_uris": [
        "http://localhost:8000/dashboard",
        "http://localhost:3000",
        "https://tm-store-api-releases-tuanmjnh.vercel.app",
        "https://tm-store-quasar-vite-releases.vercel.app",
        "https://nodejs-google-drive-oauth-desktop.vercel.app"
      ],
      "javascript_origins": [
        "http://localhost:8000",
        "http://localhost:3000",
        "https://tm-store-quasar-vite-releases.vercel.app",
        "https://tm-store-api-releases-tuanmjnh.vercel.app",
        "https://nodejs-google-drive-oauth-desktop.vercel.app"
      ]
    }
  },
  "credentials": {
    "access_token": "ya29.a0AfB_byClG5rzg-O3tZH75tbu87atP5do94zMWbrmaZSIbUpxuMMac0lPXWu9AuZ7BSatuSErtfCIXx5ljin4owValtWib6WXQjimig9NZTrcpdlCpBr0Gs9ZBj5CX_v_huEMlZ4_h6-zIX55r7nTyzNyZcKwyvAPrh2YaCgYKAXkSARMSFQGOcNnChM4q4MarO_3C9kEdF-XaWA0171",
    "refresh_token": "1//0e5kj0--LF2uJCgYIARAAGA4SNwF-L9IrxTB1Wqc6flBj7I6iv3ljUBIRpobKiMC9xX3y7VBwilRAyfsOpfnr1YKJkodPq1JSKlE",
    "scope": "https://www.googleapis.com/auth/drive.appdata https://www.googleapis.com/auth/drive https://www.googleapis.com/auth/drive.file https://www.googleapis.com/auth/userinfo.profile",
    "token_type": "Bearer",
    "id_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6ImY1ZjRiZjQ2ZTUyYjMxZDliNjI0OWY3MzA5YWQwMzM4NDAwNjgwY2QiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIyMzUzMjQ0NjE3NTgtbjlxczBmM2tlYzVlOHE4dDJhbG1xNmVkbjBjamg3MDQuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiIyMzUzMjQ0NjE3NTgtbjlxczBmM2tlYzVlOHE4dDJhbG1xNmVkbjBjamg3MDQuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMDE2NTIzMTcxNDUxMDU2Mjc0OTUiLCJhdF9oYXNoIjoib0Izb2RMT3MwWXk2eWFhN1FDMzhwQSIsIm5hbWUiOiJ0dWFubWpuaCB0bXN0b3JlIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0t2emJqWl9FYURuaGZZTmV3YTNMamVlbTNiZktoRTFHYlo4VHpkRFZqWjVRPXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6InR1YW5tam5oIiwiZmFtaWx5X25hbWUiOiJ0bXN0b3JlIiwibG9jYWxlIjoiZW4iLCJpYXQiOjE2OTkyNTQwODYsImV4cCI6MTY5OTI1NzY4Nn0.LxpNRoWv2uF1HCft4EC6oAHTx7uIp-eNWkv6cTa9wwWrkSa0A8YNfg2XL-mBcDiKSSitrnX5bOoI2AuX6b7ff_kk_b8zz_1ZzYsEkR55zPRIT-H4GzeLxVfUp4K-HJEpjcofc8bRmrpUSrtG-YilPQVqrQXRf1b9uL8DIUEicB8UBobAuSeB_m3AAk1eSj_wXCvehG3OtdGu7EmrYfVYueWj_zVEUQ-yy7rYRPmH-xBYBZwuTmQGjHq42qWY6Ml5Es5WWsv-sqQAlLJYKlJUOxzIB3qYr08RDwHBJhanGxnIJbCJ8pNOLQVFS7c9Qd2KLEtcbsxrCTywOcJ8v89iyA",
    "expiry_date": {
      "$numberDouble": "1699257681347.0"
    },
    "type": "authorized_user",
    "client_id": "235324461758-n9qs0f3kec5e8q8t2almq6edn0cjh704.apps.googleusercontent.com",
    "client_secret": "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"
  },
  "authUri": null,
  "redirectUris": null,
  "profile": {
    "iss": "https://accounts.google.com",
    "azp": "235324461758-n9qs0f3kec5e8q8t2almq6edn0cjh704.apps.googleusercontent.com",
    "aud": "235324461758-n9qs0f3kec5e8q8t2almq6edn0cjh704.apps.googleusercontent.com",
    "sub": "101652317145105627495",
    "at_hash": "oB3odLOs0Yy6yaa7QC38pA",
    "name": "tuanmjnh tmstore",
    "picture": "https://lh3.googleusercontent.com/a/ACg8ocKvzbjZ_EaDnhfYNewa3Ljeem3bfKhE1GbZ8TzdDVjZ5Q=s96-c",
    "given_name": "tuanmjnh",
    "family_name": "tmstore",
    "locale": "en",
    "iat": {
      "$numberInt": "1699254086"
    },
    "exp": {
      "$numberInt": "1699257686"
    }
  },
  "flag": {
    "$numberInt": "1"
  },
  "created": {
    "at": {
      "$date": {
        "$numberLong": "1699239977742"
      }
    },
    "by": "admin",
    "ip": ""
  },
  "config": {
    "FOLDER_ROOT": "1DFDqKNAf2pCR_PFu3iS1gtMyGRWgf8jV",
    "EMAIL_ROOT": "minhtuan200990tmstore@gmail.com"
  }
});
