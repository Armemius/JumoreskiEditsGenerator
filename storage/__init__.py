from storage.base import engine, Base

# Preload all models to ensure they are registered with the metadata
import storage.models  # noqa: F401

Base.metadata.create_all(engine)
