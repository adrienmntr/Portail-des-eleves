from django.db import models
from django.utils.text import slugify

from authentication.models import User


class ReviewForm(models.Model):
    """
    Generic object for storing a form
    * Many courses can use this form
    * Many question can reference to this form

    Attributes
    ----------
    id
    date: Date at which the item was created
    """

    id = models.AutoField(unique=True, primary_key=True)

    date = models.DateTimeField(auto_now_add=True)


class Course(models.Model):
    """
    Object for storing Courses

    Attributes
    ----------
    id
    name: name of the course
    review_form:
    """

    id = models.AutoField(unique=True, primary_key=True)

    name = models.CharField(max_length=128)

    review_form = models.ForeignKey(
        ReviewForm,
        on_delete=models.CASCADE,
    )


class CourseMedia(models.Model):
    name = models.CharField(max_length=128, unique=True)

    uploaded_on = models.DateTimeField(auto_now_add=True)

    category = models.CharField(max_length=64)

    file = models.FileField(upload_to='courses/')

    iploaded_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
    )


NUMERIC_SCALE = (
    (1, ('VERY_UNSATISFIED')),
    (2, ('UNSATISFIED')),
    (3, ('NEUTRAL')),
    (4, ('SATISFIED')),
    (5, ('VERY_SATISFIED')),
)


class Rating(models.Model):
    """
    User's rate for a field

    Attributes
    ----------
    id
    required
    name: what will be displayed to the User
    review_form: associated form

    Notes
    -----
    You could imagine different kinds of scales
    https://www.questionpro.com/blog/rating-scale/
    """

    id = models.AutoField(primary_key=True, unique=True)

    required = models.BooleanField(default=False)

    category = models.CharField(max_length=64)

    review_form = models.ForeignKey(
        ReviewForm,
        on_delete=models.CASCADE,
    )


class UserRating(models.Model):
    """
    User answer to a rating

    Attributes
    ----------
    id
    value:
    course:
    rating:
    """

    id = models.AutoField(primary_key=True, unique=True)

    value = models.PositiveSmallIntegerField(choices=NUMERIC_SCALE)

    rating = models.ForeignKey(
        Rating,
        on_delete=models.CASCADE,
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
    )


class Comment(models.Model):
    """
    User's rate for a field

    Attributes
    ----------
    id
    required
    name: what will be displayed to the User
    review_form: associated form
    """

    id = models.AutoField(primary_key=True, unique=True)

    category = models.CharField(max_length=64)

    required = models.BooleanField(default=False)

    review_form = models.ForeignKey(
        ReviewForm,
        on_delete=models.CASCADE,
    )


class UserComment(models.Model):
    """
    User answer to a rating

    Attributes
    ----------
    id
    comment
    course:
    rating:
    """

    id = models.AutoField(primary_key=True, unique=True)

    content = models.CharField(
        max_length=128,
        blank=True,
    )

    comment = models.ForeignKey(
        Rating,
        on_delete=models.CASCADE,
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
    )


class HasVoted(models.Model):
    """
    Controls if a user has voted
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
    )