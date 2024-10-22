```mermaid
graph TD
    A[CodeSandbox] --> B[Frontend: HTML, CSS, JavaScript]
    B --> C[UI Components]
    C --> D[Game Board (HTML Table)]
    C --> E[Styles (CSS)]
    B --> F[Game Logic (JavaScript)]
    F --> G[Player Input Handling]
    F --> H[Game Rules Engine]
    F --> I[Move Validation]
    F --> J[AI Player Logic (Optional)]
    F --> K[In-Memory Database (JavaScript Object)]
    G --> K
    I --> K
    H --> K
    J --> K
    B --> L[Rendering and Animation]
    D --> L
    E --> L
    K --> M[Game State Management]
    M --> L
    M --> N[Update Game Board]
    N --> D
```