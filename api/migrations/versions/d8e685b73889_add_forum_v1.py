"""ADD forum v1

Revision ID: d8e685b73889
Revises: 9ced7348c1b7
Create Date: 2023-07-16 15:48:35.080037

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "d8e685b73889"
down_revision = "9ced7348c1b7"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "forum_category",
        sa.Column(
            "id",
            mysql.VARCHAR(
                charset="utf8mb4", collation="utf8mb4_general_ci", length=36
            ),
            nullable=False,
        ),
        sa.Column(
            "name",
            mysql.VARCHAR(
                charset="utf8mb4", collation="utf8mb4_general_ci", length=128
            ),
            nullable=True,
        ),
        sa.Column(
            "course_id",
            mysql.VARCHAR(
                charset="utf8mb4", collation="utf8mb4_general_ci", length=36
            ),
            nullable=True,
        ),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("last_updated", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["course_id"],
            ["course.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        mysql_charset="utf8mb4",
        mysql_collate="utf8mb4_general_ci",
    )
    with op.batch_alter_table("forum_category", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_forum_category_id"), ["id"], unique=False
        )

    op.create_table(
        "forum_post",
        sa.Column(
            "id",
            mysql.VARCHAR(
                charset="utf8mb4", collation="utf8mb4_general_ci", length=36
            ),
            nullable=False,
        ),
        sa.Column(
            "owner_id",
            mysql.VARCHAR(
                charset="utf8mb4", collation="utf8mb4_general_ci", length=36
            ),
            nullable=False,
        ),
        sa.Column(
            "course_id",
            mysql.VARCHAR(
                charset="utf8mb4", collation="utf8mb4_general_ci", length=36
            ),
            nullable=True,
        ),
        sa.Column("visible_to_students", sa.Boolean(), nullable=True),
        sa.Column("pinned", sa.Boolean(), nullable=True),
        sa.Column("anonymous", sa.Boolean(), nullable=True),
        sa.Column("seen_count", sa.Integer(), nullable=True),
        sa.Column(
            "title",
            mysql.TEXT(collation="utf8mb4_general_ci", length=1024),
            nullable=True,
        ),
        sa.Column(
            "content",
            mysql.JSON(),
            nullable=True,
        ),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("last_updated", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["course_id"],
            ["course.id"],
        ),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        mysql_charset="utf8mb4",
        mysql_collate="utf8mb4_general_ci",
    )
    with op.batch_alter_table("forum_post", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_forum_post_id"), ["id"], unique=False
        )

    op.create_table(
        "forum_post_comment",
        sa.Column(
            "id",
            mysql.VARCHAR(
                charset="utf8mb4", collation="utf8mb4_general_ci", length=36
            ),
            nullable=False,
        ),
        sa.Column(
            "owner_id",
            mysql.VARCHAR(
                charset="utf8mb4", collation="utf8mb4_general_ci", length=36
            ),
            nullable=False,
        ),
        sa.Column(
            "post_id",
            mysql.VARCHAR(
                charset="utf8mb4", collation="utf8mb4_general_ci", length=36
            ),
            nullable=False,
        ),
        sa.Column(
            "parent_id",
            mysql.VARCHAR(
                charset="utf8mb4", collation="utf8mb4_general_ci", length=36
            ),
            nullable=True,
        ),
        sa.Column(
            "approved_by_id",
            mysql.VARCHAR(
                charset="utf8mb4", collation="utf8mb4_general_ci", length=36
            ),
            nullable=True,
        ),
        sa.Column("anonymous", sa.Boolean(), nullable=True),
        sa.Column("thread_start", sa.Boolean(), nullable=True),
        sa.Column(
            "content",
            mysql.JSON(),
            nullable=True,
        ),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("last_updated", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["approved_by_id"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["post_id"],
            ["forum_post.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        mysql_charset="utf8mb4",
        mysql_collate="utf8mb4_general_ci",
    )
    with op.batch_alter_table("forum_post_comment", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_forum_post_comment_id"), ["id"], unique=False
        )

    op.create_table(
        "forum_post_in_category",
        sa.Column(
            "post_id",
            mysql.VARCHAR(
                charset="utf8mb4", collation="utf8mb4_general_ci", length=36
            ),
            nullable=False,
        ),
        sa.Column(
            "category_id",
            mysql.VARCHAR(
                charset="utf8mb4", collation="utf8mb4_general_ci", length=36
            ),
            nullable=False,
        ),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("last_updated", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["category_id"],
            ["forum_category.id"],
        ),
        sa.ForeignKeyConstraint(
            ["post_id"],
            ["forum_post.id"],
        ),
        sa.PrimaryKeyConstraint("post_id", "category_id"),
        mysql_charset="utf8mb4",
        mysql_collate="utf8mb4_general_ci",
    )
    op.create_table(
        "forum_post_upvote",
        sa.Column(
            "id",
            mysql.VARCHAR(
                charset="utf8mb4", collation="utf8mb4_general_ci", length=36
            ),
            nullable=False,
        ),
        sa.Column(
            "owner_id",
            mysql.VARCHAR(
                charset="utf8mb4", collation="utf8mb4_general_ci", length=36
            ),
            nullable=False,
        ),
        sa.Column(
            "post_id",
            mysql.VARCHAR(
                charset="utf8mb4", collation="utf8mb4_general_ci", length=36
            ),
            nullable=False,
        ),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("last_updated", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["post_id"],
            ["forum_post.id"],
        ),
        sa.PrimaryKeyConstraint("id", "owner_id", "post_id"),
        mysql_charset="utf8mb4",
        mysql_collate="utf8mb4_general_ci",
    )
    with op.batch_alter_table("forum_post_upvote", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_forum_post_upvote_id"), ["id"], unique=False
        )

    op.create_table(
        "forum_post_viewed",
        sa.Column(
            "owner_id",
            mysql.VARCHAR(
                charset="utf8mb4", collation="utf8mb4_general_ci", length=36
            ),
            nullable=False,
        ),
        sa.Column(
            "post_id",
            mysql.VARCHAR(
                charset="utf8mb4", collation="utf8mb4_general_ci", length=36
            ),
            nullable=False,
        ),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("last_updated", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["post_id"],
            ["forum_post.id"],
        ),
        sa.PrimaryKeyConstraint("owner_id", "post_id"),
        mysql_charset="utf8mb4",
        mysql_collate="utf8mb4_general_ci",
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("forum_post_viewed")
    with op.batch_alter_table("forum_post_upvote", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_forum_post_upvote_id"))

    op.drop_table("forum_post_upvote")
    op.drop_table("forum_post_in_category")
    with op.batch_alter_table("forum_post_comment", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_forum_post_comment_id"))

    op.drop_table("forum_post_comment")
    with op.batch_alter_table("forum_post", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_forum_post_id"))

    op.drop_table("forum_post")
    with op.batch_alter_table("forum_category", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_forum_category_id"))

    op.drop_table("forum_category")
    # ### end Alembic commands ###
