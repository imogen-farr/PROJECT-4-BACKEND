from django.db import models


class Comment(models.Model):
    # Explain that it's text as it's a bigger box in admin view
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    pet = models.ForeignKey(
        # this defines where the relationship is - in the pets app on the Pet model
        "pets.Pet",
        related_name="comments",  # This is what the column will be called on the album lookup
        # This specifies that the comment should be deleted if the pet is deleted
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        "jwt_auth.User",
        related_name="comments",
        on_delete=models.CASCADE
    )
