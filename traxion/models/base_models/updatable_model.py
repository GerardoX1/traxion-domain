from time import time

from pydantic import BaseModel, ConfigDict, PositiveInt


class UpdatableModel(BaseModel):
    """
    `updated_copy()` method that creates a new object with updated fields, 
    automatically refreshing the `updated_at` timestamp.
    """

    updated_at: PositiveInt
    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)

    def updated_copy(self, data: dict) -> "UpdatableModel":
        """
        Creates and returns a new instance by merging the current instance's fields
        with the given `data`, setting `updated_at` to the current time in milliseconds.

        Args:
            data (dict): A dictionary containing the fields to be updated.

        Returns:
            UpdatableModel: A **new** instance of the model with the updates applied.

        Example:
            >>> old_model = UpdatableModel(updated_at=1234567890)
            >>> new_model = old_model.updated_copy({"name": "NewName"})
            >>> assert old_model is not new_model
        """
        updated_data = {
            **self.model_dump(),
            **data,
            "updated_at": round(time() * 1000),
        }
        return self.model_validate(updated_data)
