**DECISIONS.md must include:**
- Features completed and why
- Features skipped and why
- Time allocation breakdown
- Technical challenges faced
- Trade-offs made
- What you would add with more time
- Justification for using Django templates for the frontend


Decido usar como imagen base de django FROM	python:3.11-slim en vez
de python 3.13.7, la verison más reciente de Python para una carga 
mas rapida del contenedor. Pasando de 90.7s a 32.9s de construcción y una imagen de 1.16GB a una de 183MB