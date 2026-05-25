from fastapi import APIRouter

router = APIRouter(tags=["Organizations"])


ORGANIZATIONS = [
    {
        "name": "GenomeX Labs",
        "type": "Research"
    },
    {
        "name": "BioSecure Hospital",
        "type": "Healthcare"
    }
]


@router.get("/organizations")
def get_organizations():
    return {
        "organizations": ORGANIZATIONS
    }