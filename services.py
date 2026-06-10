from accounts.models import User


def calculer_compatibilite(mentor, mentoré):
    score = 0

    # matières
    matieres_communes = set(
        mentor.matieres.values_list('id', flat=True)
    ) & set(
        mentoré.matieres.values_list('id', flat=True)
    )

    score += len(matieres_communes) * 15

    # compétences
    competences_communes = set(
        mentor.competences.values_list('id', flat=True)
    ) & set(
        mentoré.competences.values_list('id', flat=True)
    )

    score += len(competences_communes) * 10

    # disponibilités
    disponibilites_communes = set(
        mentor.disponibilites.values_list('id', flat=True)
    ) & set(
        mentoré.disponibilites.values_list('id', flat=True)
    )

    score += len(disponibilites_communes) * 20

    # établissement
    if mentor.etablissement == mentoré.etablissement:
        score += 15

    # niveau
    if mentor.niveau_etude == mentoré.niveau_etude:
        score += 10

    return 85