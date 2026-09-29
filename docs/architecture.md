# Project Design Diagrams

## 1. System Architecture

```mermaid
flowchart TD

    U[User]

    GUI[GUI Layer<br>gui.py]

    PM[PDF Manager<br>pdf_manager.py]

    V[PDF Validator<br>pdf_validator.py]

    I[PDF Information<br>pdf_info.py]

    S[PDF Security<br>pdf_security.py]

    H[History Manager<br>history_manager.py]

    P[pypdf Library]

    O[Protected / Merged PDF]

    J[history.json]

    U --> GUI

    GUI --> PM

    PM --> V
    PM --> I
    PM --> S

    PM --> P

    S --> P
    V --> P
    I --> P

    PM --> H

    H --> J

    P --> O

## 2. system workflow
flowchart TD

    A([START])

    B[Select PDF Files]

    C{Are PDFs Valid?}

    D[Display Error]

    E[Display PDF Information]

    F[Arrange PDF Order]

    G[Enter Password]

    H{Passwords Valid?}

    I[Display Password Error]

    J[Merge PDFs]

    K[Encrypt Final PDF]

    L[Save Output PDF]

    M[Record Operation in History]

    N[Display Success Message]

    O([END])

    A --> B
    B --> C

    C -- No --> D
    D --> B

    C -- Yes --> E
    E --> F
    F --> G
    G --> H

    H -- No --> I
    I --> G

    H -- Yes --> J
    J --> K
    K --> L
    L --> M
    M --> N
    N --> O

## function module architecture
flowchart LR

    GUI[Graphical User Interface]

    VALIDATOR[PDF Validation]
    INFO[PDF Information]
    MANAGER[PDF Processing]
    SECURITY[PDF Security]
    HISTORY[History Management]

    GUI --> VALIDATOR
    GUI --> INFO
    GUI --> MANAGER
    GUI --> SECURITY
    GUI --> HISTORY

    VALIDATOR --> PDF[pypdf]
    INFO --> PDF
    MANAGER --> PDF
    SECURITY --> PDF

    HISTORY --> JSON[history.json]

## 4. 