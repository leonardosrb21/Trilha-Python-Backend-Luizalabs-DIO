from fastapi import FastAPI
from workout_api.atleta.controller import router as atleta_router
from workout_api.categorias.controller import router as categoria_router
from workout_api.centro_treinamento.controller import router as centro_router

app = FastAPI(title='WorkoutAPI')

app.include_router(atleta_router, prefix='/atletas', tags=['atletas'])
app.include_router(categoria_router, prefix='/categorias', tags=['categorias'])
app.include_router(centro_router, prefix='/centros_treinamento', tags=['centros_treinamento'])