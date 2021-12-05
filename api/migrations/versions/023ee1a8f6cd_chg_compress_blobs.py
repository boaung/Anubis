"""CHG compress blobs

Revision ID: 023ee1a8f6cd
Revises: 2e9cae7411e6
Create Date: 2021-12-05 10:47:10.420875

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "023ee1a8f6cd"
down_revision = "2e9cae7411e6"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "static_file",
        sa.Column("_blob", sa.LargeBinary(length=4294967295), nullable=True),
    )
    op.add_column(
        "submission_build", sa.Column("_stdout", sa.LargeBinary(65535), nullable=True)
    )
    op.add_column(
        "submission_test_result",
        sa.Column("_stdout", sa.LargeBinary(65535), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("submission_test_result", "_stdout")
    op.drop_column("submission_build", "_stdout")
    op.drop_column("static_file", "_blob")
    # ### end Alembic commands ###
