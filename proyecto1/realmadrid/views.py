from django.shortcuts import render


def jugadores(request):
    listajugadores=[
        {
            "Nombre":"Sergio Ramos",
            "Demarcacion":"Defensa",
            "Numero":5,
            "Foto": "foto1.jpg"
        },
        {
            "Nombre": "Eden Hazard",
            "Demarcacion": "Delantero",
            "Numero":7,
            "Foto": "foto2.jpg"
        },
        {
            "Nombre": "Karim Benzema",
            "Demarcacion": "Delantero",
            "Numero":9,
            "Foto": "foto3.jpg"
        },
        {
            "Nombre": "Toni Kroos",
            "Demarcacion": "Centrocampista",
            "Numero":8,
            "Foto": "foto4.jpg"
        },
        {
            "Nombre": "Thibaut Courtois",
            "Demarcacion": "Portero",
            "Numero": 1,
            "Foto": "foto5.jpg"
        }
    ]
    contexto = {
        'listado_jugadores': listajugadores
    }
    return render(request, "realmadrid/jugadores.html",contexto)