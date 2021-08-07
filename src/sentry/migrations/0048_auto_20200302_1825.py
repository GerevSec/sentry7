# Generated by Django 1.11.28 on 2020-03-02 19:55

from django.db import migrations
import django.db.models.deletion
import sentry.db.models.fields.bounded
import sentry.db.models.fields.foreignkey


class Migration(migrations.Migration):
    # This flag is used to mark that a migration shouldn't be automatically run in
    # production. We set this to True for operations that we think are risky and want
    # someone from ops to run manually and monitor.
    # General advice is that if in doubt, mark your migration as `is_dangerous`.
    # Some things you should always mark as dangerous:
    # - Large data migrations. Typically we want these to be run manually by ops so that
    #   they can be monitored. Since data migrations will now hold a transaction open
    #   this is even more important.
    # - Adding columns to highly active tables, even ones that are NULL.
    is_dangerous = False

    # This flag is used to decide whether to run this migration in a transaction or not.
    # By default we prefer to run in a transaction, but for migrations where you want
    # to `CREATE INDEX CONCURRENTLY` this needs to be set to False. Typically you'll
    # want to create an index concurrently when adding one to an existing table.
    atomic = True

    dependencies = [("sentry", "0047_auto_20200224_2319")]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.RemoveField(model_name="organizationonboardingtask", name="project_id"),
                migrations.AddField(
                    model_name="organizationonboardingtask",
                    name="project",
                    field=sentry.db.models.fields.foreignkey.FlexibleForeignKey(
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sentry.Project",
                    ),
                ),
                migrations.AlterField(
                    model_name="organizationonboardingtask",
                    name="status",
                    field=sentry.db.models.fields.bounded.BoundedPositiveIntegerField(
                        choices=[(1, "complete"), (2, "pending"), (3, "skipped")]
                    ),
                ),
                migrations.AlterField(
                    model_name="organizationonboardingtask",
                    name="task",
                    field=sentry.db.models.fields.bounded.BoundedPositiveIntegerField(
                        choices=[
                            (1, "create_project"),
                            (2, "send_first_event"),
                            (3, "invite_member"),
                            (4, "setup_second_platform"),
                            (5, "setup_user_context"),
                            (6, "setup_release_tracking"),
                            (7, "setup_sourcemaps"),
                            (8, "setup_user_reports"),
                            (9, "setup_issue_tracker"),
                            (10, "setup_alert_rules"),
                        ]
                    ),
                ),
            ]
        )
    ]