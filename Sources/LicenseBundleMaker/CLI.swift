import ArgumentParser

@main
struct CLI: ParsableCommand {
    @Argument()
    var action: String

    mutating func run() throws {
        print("LicenseBundleMaker")

        if action == "generate" {
            print("API creation is not supported.")
        }
    }
}
