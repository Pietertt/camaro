# Camaro beveiligingscamara

Louter vreugde voor dit fantastische project. Een paar instructies:

## Installatie

Pull eerst de repo met deze commands.

```bash
git init
git remote add origin https://github.com/Pietertt/camaro.git
git pull origin master
```

Start de stack met
```
docker-compose -f docker-compose.dev.yml up -d 
```

Optioneel kunnen de Keras en de promo website gestart worden met
```
docker-compose -f docker-compose.prod.yml up -d 
```

Start alle containers met 
```
docker-compose -f docker-compose.prod.yml -f docker-compose.dev.yml up -d 
```