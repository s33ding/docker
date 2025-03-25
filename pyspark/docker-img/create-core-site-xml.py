import os
import json
import boto3

CORE_SITE_FILENAME = "core-site.xml"

def get_spark_secret():
    """Retrieve the 'spark' secret from AWS Secrets Manager."""
    client = boto3.client('secretsmanager')

    try:
        response = client.get_secret_value(SecretId="spark")
        secret = json.loads(response['SecretString'])
        return secret
    except Exception as e:
        print(f"❌ Failed to retrieve secret: {e}")
        return None

def create_core_site_xml(secret):
    """Generate core-site.xml in the current working directory."""
    config_content = f"""<configuration>
    <property>
        <name>fs.s3a.impl</name>
        <value>org.apache.hadoop.fs.s3a.S3AFileSystem</value>
    </property>
    <property>
        <name>fs.s3a.access.key</name>
        <value>{secret['AWS_ACCESS_KEY_ID']}</value>
    </property>
    <property>
        <name>fs.s3a.secret.key</name>
        <value>{secret['AWS_SECRET_ACCESS_KEY']}</value>
    </property>
    <property>
        <name>fs.s3a.endpoint</name>
        <value>s3.amazonaws.com</value>
    </property>
    <property>
        <name>fs.s3a.path.style.access</name>
        <value>true</value>
    </property>
    <property>
        <name>fs.s3a.fast.upload</name>
        <value>true</value>
    </property>
</configuration>"""

    try:
        # Write the configuration file in the current folder
        with open(CORE_SITE_FILENAME, "w") as file:
            file.write(config_content)

        # Set file permissions
        os.chmod(CORE_SITE_FILENAME, 0o644)

        print(f"✅ Successfully created: {os.path.abspath(CORE_SITE_FILENAME)}")

    except Exception as e:
        print(f"❌ Error writing {CORE_SITE_FILENAME}: {e}")

def main():
    print("🔍 Retrieving Spark secrets from AWS Secrets Manager ...")

    secret = get_spark_secret()
    if secret:
        create_core_site_xml(secret)
    else:
        print("❌ Could not fetch secrets. Exiting.")

if __name__ == "__main__":
    main()

